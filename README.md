# Kyte API Python Library

The Kyte API Python Library is designed to facilitate communication between a Python client and the Kyte API endpoint. It simplifies the process of authentication, request signing, and making API calls.

## Installation

You can install the Kyte API Python Library using `pip`:

```bash
pip install kyte
```

## Usage

### Initialization

```python
from kyte import api

# Initialize the Kyte API client
client = api(public_key, private_key, kyte_account, kyte_identifier, kyte_endpoint)
```

### Making Requests

#### Create Session

```python
# Creating a session
client.createSession(username, password)
```

#### Make GET Request

```python
# Making a GET request
result = client.get(model, field, value, headers)
```

#### Make POST Request

```python
# Making a POST request
result = client.post(model, data, headers)
```

#### Make PUT Request

```python
# Making a PUT request
result = client.put(model, field, value, data, headers)
```

#### Make DELETE Request

```python
# Making a DELETE request
result = client.delete(model, field, value, headers)
```

### Additional Information

- `model`: The specific model for the API endpoint.
- `field` and `value`: Optional parameters for filtering.
- `data`: Payload for POST and PUT requests.
- `headers`: Additional headers to be included in the request.

## Example

```python
# Example usage
client = api(public_key, private_key, kyte_account, kyte_identifier, kyte_endpoint)
client.createSession(username, password)
result = client.get("example_model", "example_field", "example_value", {'Custom-Header': 'Value'})
```

## Testing Locally

You can install the package locally by:
```python
pip install .
```

If you have an existing install, you can update the package and depenencies by:
```python
pip install --upgrade .
```

Lastly, to uninstall the package, use the package name
```python
pip uninstall kyte
```

## Creating a Source Distribution

For all Python projects, it's advisable to offer a source distribution.

PyPI mandates specific metadata that should be included in your setup.py file. To ensure your project meets these requirements, run:

```bash
python setup.py check
```

If no issues are reported, your package is considered compliant.

To create a source distribution, execute the following command from your root directory:

```bash
python setup.py sdist
```

## Creating a Wheel Distribution

You have the option to generate a wheel distribution, which is a pre-built distribution tailored for the current platform.

If you don't have the wheel package, you can install it via pip:

```bash
pip install wheel
```

There are various types of wheels available. For a project that's purely Python and compatible with both Python 2 and 3, you can create a universal wheel:

```bash
python setup.py bdist_wheel --universal
```

For projects that aren't Python 2/3 compatible or contain compiled extensions, use the following command:

```bash
python setup.py bdist_wheel
```

The installable wheel will be generated within the `dist/` directory, and a separate build directory will contain the compiled code.

## Publishing on PyPI

Install twine if not already available:
```python
pip install twine
```

### Uploading to testpypi

Before making the package available publicly, it is best to test the upload and install using testpypi. To upload to testpypi, run
```python
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

You can alternatively specify the source distribution instead of uploading all generated distributions in the `dist/` directory.

To test install from testpypi, run:
```python
pip install --index-url https://test.pypi.org/simple/ kyte --user
```

### Uploading to PyPI

Once you've completed the test above, you can upload the package to PyPI using:
```python
twine upload dist/*
```

And test the install using:
```python
pip install kyte --user
```

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests in the [GitHub repository](https://github.com/keyqcloud/kyte-api-python).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

