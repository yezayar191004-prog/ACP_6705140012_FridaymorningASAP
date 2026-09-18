from ac import AirConditioner

results = []
def check(name, fn):
    try:
        fn(); results.append((name, True, ""))
    except AssertionError as e:
        results.append((name, False, str(e) or "assertion failed"))
    except Exception as e:
        results.append((name, False, f"{type(e).__name__}: {e}"[:80]))

def c1():
    ac = AirConditioner("Daikin", "Bedroom")
    assert "Bedroom" in str(ac)
check("1. Builds and __str__ works", c1)

def c2():
    ac = AirConditioner("Daikin", "Bedroom"); ac.temperature = 22
    assert ac.temperature == 22
check("2. A valid temperature is stored", c2)

def c3():
    ac = AirConditioner("Daikin", "Bedroom")
    ac.temperature = 22; assert ac.is_energy_saving is False
    ac.temperature = 26; assert ac.is_energy_saving is True
check("3. is_energy_saving reflects the CURRENT temperature", c3)

def c4():
    ac = AirConditioner("Daikin", "Bedroom")
    for bad in (5, 40):
        try: ac.temperature = bad; assert False, f"accepted {bad}"...
