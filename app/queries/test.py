from conDB import *

def test_1():
    con = connectionDB()
    row = con.execute("select release_version from system.local").one()
    return str(row)