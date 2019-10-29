from printer import Printer
from system import System
from job import Job
from random import randrange

impresora_1 = Printer('001', 'Xerox Staff')
impresora_1.add_job(Job('Trabajo 1', randrange(1, 10)))
impresora_1.add_job(Job('Trabajo 2', randrange(1, 10)))
impresora_1.add_job(Job('Trabajo 3', randrange(1, 10)))
impresora_1.add_job(Job('Trabajo 4', randrange(1, 10)))
print()

impresora_2 = Printer('002', 'Xerox StaffSenior')
impresora_2.add_job(Job('Trabajo 1', randrange(1,10)))
impresora_2.add_job(Job('Trabajo 2', randrange(1,10)))
print()

impresora_3 = Printer('003', 'Xerox Gerentes')
impresora_3.add_job(Job('Trabajo 1', randrange(1,10)))
impresora_3.add_job(Job('Trabajo 2', randrange(1,10)))
impresora_3.add_job(Job('Trabajo 3', randrange(1,10)))
print()

impresora_4 = Printer('004', 'Xerox Socios')
impresora_4.add_job(Job('Trabajo 1', randrange(1,10)))
print()

sistema = System()
print()

sistema.attach(impresora_1)
sistema.attach(impresora_2)
sistema.attach(impresora_3)
sistema.attach(impresora_4)
print()

sistema.start_print()