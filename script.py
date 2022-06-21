import pyfiglet
import typer

app = typer.Typer()


@app.command()
def wifi(
        ssid: str = typer.Option(..., prompt=True),
        password: str = typer.Option(..., prompt=True)
):
    filename = 'wifi-creds.txt'
    # Read in the file
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the target strings
    filedata = filedata.replace('{{ssid}}', ssid).replace('{{password}}', password)

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(filedata)


@app.command()
def foobar(
        foo: str = typer.Option(..., prompt=True),
        bar: str = typer.Option(..., prompt=True)
):
    print(foo)
    print(bar)


# https://typer.tiangolo.com/
if __name__ == "__main__":
    print(pyfiglet.figlet_format("AWS DeepRacer"))
    app()
