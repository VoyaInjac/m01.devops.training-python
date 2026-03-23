from demo_project import calculator


def test_integration_workflow():
    # Simulate a workflow using multiple operations
    a = 3
    b = 10
    result = calculator.add(a, b)
    result = calculator.multiply(result, 2)
    result = calculator.subtract(result, 10)
    result = calculator.divide(result, 4)
    assert result == 4
