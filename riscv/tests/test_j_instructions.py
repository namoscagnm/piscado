"""
Tests J type instructions
"""
from riscv.risc_machine import RiscMachine
from riscv.compiler import RiscCompiler


def test_jal():
    """
    Tests jump and link instruction
    """
    rc = RiscCompiler()
    rc.enter_input("JAL", "x1", 2)
    rc.enter_input("ADD", "x5", "x0", "x10")
    rc.enter_input("ADDI", "x10", "x0", 1000)
    rc.enter_input("JAL", "x0", -2)

    program_memory = rc.createoutput()
    rm = RiscMachine(program=program_memory)
    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()

    assert rm.inspect_register("x5") == 1000
