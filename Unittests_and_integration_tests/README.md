## Resources

****Read or watch:****

*   [unittest — Unit testing framework](/rltoken/ug8beURP6GPP7yJtQ4I1Jw "unittest — Unit testing framework")
*   [unittest.mock — mock object library](/rltoken/cCjj8L1q_NaYxvFfqFfYPA "unittest.mock — mock object library")
*   [How to mock a readonly property with mock?](/rltoken/y8OnTBcqkL_Rmr2I3peRSQ "How to mock a readonly property with mock?")
*   [parameterized](/rltoken/Z6XhDNPKVcd7BW6163H0_Q "parameterized")
*   [Memoization](/rltoken/7xU6wdKJpB8L2S8vtkxpjw "Memoization")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/AiD51mZh2lZ8stCrg3CjGQ "explain to anyone"), **without the help of Google**:

*   The difference between unit and integration tests.
*   Common testing patterns such as mocking, parametrizations and fixtures

## Requirements

*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/env python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the `pycodestyle` style (version 2.5)
*   All your files must be executable
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   All your functions and coroutines must be type-annotated.

## Tasks

### 1.

Familiarize yourself with the `utils.access_nested_map` function and understand its purpose. Play with it in the Python console to make sure you understand.

In this task you will write the first unit test for `utils.access_nested_map`.

Create a `TestAccessNestedMap` class that inherits from `unittest.TestCase`.

Implement the `TestAccessNestedMap.test_access_nested_map` method to test that the method returns what it is supposed to.

Decorate the method with `@parameterized.expand` to test the function for following inputs:
```
nested\_map={"a": 1}, path=("a",)
nested\_map={"a": {"b": 2}}, path=("a",)
nested\_map={"a": {"b": 2}}, path=("a", "b")
```
For each of these inputs, test with `assertEqual` that the function returns the expected result.

The body of the test method should not be longer than 2 lines.

  

### 2.

Implement `TestAccessNestedMap.test_access_nested_map_exception`. Use the `assertRaises` context manager to test that a `KeyError` is raised for the following inputs (use `@parameterized.expand`):
```
nested\_map={}, path=("a",)
nested\_map={"a": 1}, path=("a", "b")
```
Also make sure that the exception message is as expected.

  

### 3.

Familiarize yourself with the `utils.get_json` function.

Define the `TestGetJson(unittest.TestCase)` class and implement the `TestGetJson.test_get_json` method to test that `utils.get_json` returns the expected result.

We don’t want to make any actual external HTTP calls. Use `unittest.mock.patch` to patch `requests.get`. Make sure it returns a `Mock` object with a `json` method that returns `test_payload` which you parametrize alongside the `test_url` that you will pass to `get_json` with the following inputs:
```
test\_url="http://example.com", test\_payload={"payload": True}
test\_url="http://holberton.io", test\_payload={"payload": False}
```
Test that the mocked `get` method was called exactly once (per input) with `test_url` as argument.

Test that the output of `get_json` is equal to `test_payload`.

  

### 4.

Read about memoization and familiarize yourself with the `utils.memoize` decorator.

Implement the `TestMemoize(unittest.TestCase)` class with a `test_memoize` method.

Inside `test_memoize`, define following class
```
class TestClass:

    def a\_method(self):
        return 42

    @memoize
    def a\_property(self):
        return self.a\_method()
```
Use `unittest.mock.patch` to mock `a_method`. Test that when calling `a_property` twice, the correct result is returned but `a_method` is only called once using `assert_called_once`.

  

### 5.

Familiarize yourself with the `client.GithubOrgClient` class.

In a new `test_client.py` file, declare the `TestGithubOrgClient(unittest.TestCase)` class and implement the `test_org` method.

This method should test that `GithubOrgClient.org` returns the correct value.

Use `@patch` as a decorator to make sure `get_json` is called once with the expected argument but make sure it is not executed.

Use `@parameterized.expand` as a decorator to parametrize the test with a couple of `org` examples to pass to `GithubOrgClient`, in this order:

*   `google`
*   `abc`

Of course, no external HTTP calls should be made.

  

### 6.

`memoize` turns methods into properties. Read up on how to mock a property (see resource).

Implement the `test_public_repos_url` method to unit-test `GithubOrgClient._public_repos_url`.

Use `patch` as a context manager to patch `GithubOrgClient.org` and make it return a known payload.

Test that the result of `_public_repos_url` is the expected one based on the mocked payload.

  

### 7.

Implement `TestGithubOrgClient.test_public_repos` to unit-test `GithubOrgClient.public_repos`.

Use `@patch` as a decorator to mock `get_json` and make it return a payload of your choice.

Use `patch` as a context manager to mock `GithubOrgClient._public_repos_url` and return a value of your choice.

Test that the list of repos is what you expect from the chosen payload.

Test that the mocked property and the mocked `get_json` was called once.

  

### 8.

Implement `TestGithubOrgClient.test_has_license` to unit-test `GithubOrgClient.has_license`.

Parametrize the test with the following inputs
```
repo={"license": {"key": "my\_license"}}, license\_key="my\_license"
repo={"license": {"key": "other\_license"}}, license\_key="my\_license"
```
You should also parameterize the expected returned value.

  

### 9.

We want to test the `GithubOrgClient.public_repos` method in an integration test. That means that we will only mock code that sends external requests.

Create the `TestIntegrationGithubOrgClient(unittest.TestCase)` class and implement the `setUpClass` and `tearDownClass` which are part of the `unittest.TestCase` API.

Use `@parameterized_class` to decorate the class and parameterize it with fixtures found in `fixtures.py`. The file contains the following fixtures:
```
org\_payload, repos\_payload, expected\_repos, apache2\_repos
```
The `setupClass` should mock `requests.get` to return example payloads found in the fixtures.

Use `patch` to start a patcher named `get_patcher`, and use `side_effect` to make sure the mock of `requests.get(url).json()` returns the correct fixtures for the various values of `url` that you anticipate to receive.

Implement the `tearDownClass` class method to stop the patcher.