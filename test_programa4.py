import pytest
from io import StringIO
from unittest.mock import patch
from programa4 import ManejadorTipos, mcm

# Instalar pytest y coverage
# pip install pytest
# pip install coverage

# Ejecutar las pruebas
# pytest test_programa4.py

# Ejecutar las pruebas con cobertura
# coverage run -m pytest test_programa4.py

# Generar el reporte de cobertura en la terminal
# coverage report

@pytest.fixture
def manejador():
    return ManejadorTipos()

def test_agregar_atomico(manejador):
    manejador.agregar_atomico("char", 1, 2)
    assert "char" in manejador.tipos
    assert manejador.tipos["char"].representacion == 1
    assert manejador.tipos["char"].alineacion == 2

def test_agregar_atomico_existente(manejador):
    manejador.agregar_atomico("char", 1, 2)
    with patch('sys.stdout', new=StringIO()) as fake_out:
        manejador.agregar_atomico("char", 1, 2)
        assert "Error: El tipo char ya existe." in fake_out.getvalue()

def test_agregar_struct(manejador):
    manejador.agregar_atomico("char", 1, 2)
    manejador.agregar_atomico("int", 4, 4)
    manejador.agregar_struct("foo", ["char", "int"])
    assert "foo" in manejador.tipos
    assert manejador.tipos["foo"].tipos == ["char", "int"]

def test_agregar_struct_existente(manejador):
    manejador.agregar_atomico("char", 1, 2)
    manejador.agregar_atomico("int", 4, 4)
    manejador.agregar_struct("foo", ["char", "int"])
    with patch('sys.stdout', new=StringIO()) as fake_out:
        manejador.agregar_struct("foo", ["char", "int"])
        assert "Error: El tipo foo ya existe." in fake_out.getvalue()

def test_agregar_struct_tipo_no_definido(manejador):
    manejador.agregar_atomico("char", 1, 2)
    with patch('sys.stdout', new=StringIO()) as fake_out:
        manejador.agregar_struct("foo", ["char", "int"])
        assert "Error: El tipo int no está definido." in fake_out.getvalue()

def test_agregar_union(manejador):
    manejador.agregar_atomico("char", 1, 2)
    manejador.agregar_atomico("int", 4, 4)
    manejador.agregar_union("bar", ["char", "int"])
    assert "bar" in manejador.tipos
    assert manejador.tipos["bar"].tipos == ["char", "int"]

def test_agregar_union_existente(manejador):
    manejador.agregar_atomico("char", 1, 2)
    manejador.agregar_atomico("int", 4, 4)
    manejador.agregar_union("bar", ["char", "int"])
    with patch('sys.stdout', new=StringIO()) as fake_out:
        manejador.agregar_union("bar", ["char", "int"])
        assert "Error: El tipo bar ya existe." in fake_out.getvalue()

def test_agregar_union_tipo_no_definido(manejador):
    manejador.agregar_atomico("char", 1, 2)
    with patch('sys.stdout', new=StringIO()) as fake_out:
        manejador.agregar_union("bar", ["char", "int"])
        assert "Error: El tipo int no está definido." in fake_out.getvalue()

def test_describir_atomico(manejador):
    manejador.agregar_atomico("char", 1, 2)
    with patch('sys.stdout', new=StringIO()) as fake_out:
        manejador.describir("char")
        assert "Tipo atómico char: Tamaño 1 bytes. Alineación 2 bytes." in fake_out.getvalue()

def test_describir_struct(manejador):
    manejador.agregar_atomico("foo", 4, 4)
    manejador.agregar_atomico("bar", 2, 2)
    manejador.agregar_atomico("baz", 4, 4)
    manejador.agregar_atomico("qux", 8, 8)
    manejador.agregar_atomico("meh", 1, 2)
    manejador.agregar_struct("meta", ["foo", "bar", "baz", "qux", "meh"])
    with patch('sys.stdout', new=StringIO()) as fake_out:
        manejador.describir("meta")
        assert "Struct meta:" in fake_out.getvalue()
        assert "Alineación: 4 bytes." in fake_out.getvalue()
        assert "Tamaño sin empaquetar: 25 bytes. Desperdicio sin empaquetar: 6 bytes." in fake_out.getvalue()
        assert "Tamaño empaquetado: 19 bytes. Desperdicio empaquetado: 0 bytes." in fake_out.getvalue()

def test_describir_union(manejador):
    manejador.agregar_atomico("foo", 4, 4)
    manejador.agregar_atomico("bar", 2, 2)
    manejador.agregar_atomico("baz", 4, 4)
    manejador.agregar_atomico("qux", 8, 8)
    manejador.agregar_atomico("meh", 1, 2)
    manejador.agregar_union("meta", ["foo", "bar", "baz", "qux", "meh"])
    with patch('sys.stdout', new=StringIO()) as fake_out:
        manejador.describir("meta")
        assert "Union meta:" in fake_out.getvalue()
        assert "Tamaño: 8 bytes. Alineación: 8 bytes." in fake_out.getvalue()
        assert "Desperdicio: El desperdicio en cualquiera de las implementaciones es a lo sumo 7 bytes." in fake_out.getvalue()


def test_describir_tipo_no_definido(manejador):
    with patch('sys.stdout', new=StringIO()) as fake_out:
        manejador.describir("foo")
        assert "Error: El tipo foo no está definido." in fake_out.getvalue()

def test_mcm():
    assert mcm(4, 6) == 12
    assert mcm(10, 15) == 30
    assert mcm(7, 3) == 21
    assert mcm(1, 1) == 1

def test_main_interaction():
    inputs = [
        "ATOMICO char 1 2",
        "ATOMICO int 4 4",
        "STRUCT foo char int",
        "UNION bar char int",
        "DESCRIBIR char",
        "DESCRIBIR foo",
        "DESCRIBIR bar",
        "SALIR"
    ]
    expected_outputs = [
        "Tipo atómico char: Tamaño 1 bytes. Alineación 2 bytes.",
        "Struct foo:",
        "Alineación: 2 bytes.",
        "Tamaño sin empaquetar: 6 bytes. Desperdicio sin empaquetar: 1 bytes.",
        "Tamaño empaquetado: 5 bytes. Desperdicio empaquetado: 0 bytes.",
        "Union bar:",
        "Tamaño: 4 bytes. Alineación: 4 bytes.",
        "Desperdicio: El desperdicio en cualquiera de las implementaciones es a lo sumo 3 bytes."
    ]
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            from programa4 import main
            main()
            output = fake_out.getvalue()
            for expected in expected_outputs:
                assert expected in output
                
# Se tiene una cobertura del 86% en programa4.py