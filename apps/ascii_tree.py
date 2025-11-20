import os
import argparse
from typing import List, Optional

def generate_tree(root: str, max_depth: Optional[int]) -> str:
    root = os.path.abspath(root)
    lines: List[str] = [f"{root}{os.sep}"]

    if max_depth is not None and max_depth <= 0:
        return "\n".join(lines)

    def format_entry(entry: os.DirEntry) -> str:
        try:
            if entry.is_symlink():
                try:
                    target = os.readlink(entry.path)
                except OSError:
                    target = "?"
                name = entry.name
                # Append slash for symlink to directory if detectable without following
                suffix = "/" if entry.is_dir(follow_symlinks=False) else ""
                return f"{name}{suffix} -> {target}"
            elif entry.is_dir(follow_symlinks=False):
                return f"{entry.name}/"
            else:
                return entry.name
        except OSError:
            return f"{entry.name} [unreadable]"

    def build(path: str, prefix: str, level: int):
        if max_depth is not None and level >= max_depth:
            return
        try:
            with os.scandir(path) as it:
                entries = list(it)
        except PermissionError:
            lines.append(prefix + "└── [Permission denied]")
            return
        except FileNotFoundError:
            lines.append(prefix + "└── [Not found]")
            return
        # Sort: directories first, then files; alphabetical case-insensitive
        entries.sort(key=lambda e: (not e.is_dir(follow_symlinks=False), e.name.lower()))
        total = len(entries)
        for idx, entry in enumerate(entries):
            connector = "└── " if idx == total - 1 else "├── "
            lines.append(prefix + connector + format_entry(entry))
            try:
                is_dir = entry.is_dir(follow_symlinks=False)
                is_link = entry.is_symlink()
            except OSError:
                is_dir = False
                is_link = False
            if is_dir and not is_link:
                extension = "    " if idx == total - 1 else "│   "
                build(entry.path, prefix + extension, level + 1)

    build(root, "", 1)
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="Write an ASCII tree of a directory to a text file."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Root directory (default: current directory)."
    )
    parser.add_argument(
        "-d", "--depth",
        type=int,
        default=None,
        help="Max depth (0 = only root, 1 = immediate children, etc.). Default: unlimited."
    )
    parser.add_argument(
        "-o", "--output",
        default="tree.txt",
        help="Output text file (default: tree.txt)."
    )
    args = parser.parse_args()

    # Normalize negative depth to unlimited
    max_depth = None if args.depth is None or args.depth < 0 else args.depth

    tree_str = generate_tree(args.path, max_depth)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(tree_str + "\n")
    print(f"Wrote tree to {args.output}")

if __name__ == "__main__":
    main()