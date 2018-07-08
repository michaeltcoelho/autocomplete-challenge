### Requirements

* Python 3.6.4.
* An activated python virtualenv.

#### Considering you have already installed the requirements:

### Installing

Clone the repository and install it:

```bash
git clone https://github.com/michaeltcoelho/autocomplete-challenge.git
```

Go to `/autocomplete-challenge` directory:

Run the following command:

```bash
make install
```

### Running

Running the application:

```bash
make run
```

### Testing

Running tests with coverage:

```bash
make test
```

### Autocomplete

Making requests to the autocomplete API:

```bash
curl -X GET -H "Content-Type: application/json" http://0.0.0.0:5000/autocomplete/?q=fac
```