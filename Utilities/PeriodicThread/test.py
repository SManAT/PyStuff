from Utilities.PeriodicThread.PeriodicThread import PeriodicThread



def Fnc():
    print("Funktion")


t = PeriodicThread(Fnc)
t.start()

