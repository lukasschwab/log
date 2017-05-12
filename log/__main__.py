import click, datetime, json
path = "/Users/lukas/Desktop/programming/log/main_log.json"

def log_simple_event(description):
    now = datetime.datetime.now()
    event = {}
    event['date'] = now.date().isoformat()
    event['time'] = now.time().isoformat()
    event['description'] = description
    record(event)

def record(event):
    out = json.dumps(event, ensure_ascii=False).encode('utf-8')
    try:
        with open(path, "a") as logfile:
            logfile.write(out)
            logfile.write("\n")
        click.echo("Logged!")
    except:
        click.echo("Write failed!")
        click.echo(out)

def delete():
    # try:
        contents = []
        with open(path, "r") as logfile:
            contents = [unicode(l, 'utf-8') for l in logfile.readlines()]
        if len(contents) == 0:
            click.echo("Nothing to undo!")
        else:
            with open(path, "w") as out:
                out.write("".join(contents[:-1]).encode('utf-8'))
                click.echo("Deleted: " + contents[-1][:-1])
    # except:
    #     click.echo("Remove failed!")
    #     click.echo()


@click.command()
@click.option("--undo", is_flag=True, help="Removes the last log entry")
def main(undo):
    click.echo(click.style(path, fg='blue'))
    if undo:
        delete()
    else:
        d = click.prompt("Describe")
        log_simple_event(d)

if __name__ == '__main__':
    main()
