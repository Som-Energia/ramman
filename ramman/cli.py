import os
import json
import click
from ramman import Ramman 

config = {
    'url': os.getenv('HEMAN_URL', None),
}

@click.group()
@click.pass_context
def (ctx):
    try:
        ctx.obj['emp'] = Ramman(ctx.obj['config'], debug=False)
    except Exception, e:
        click.echo('Heman service connection failed')

@ramman.command()
@click.pass_context
@click.argument('id', nargs=1)
@click.argument('token', nargs=1)
@click.argument('ot', nargs=1)
def get_results(ctx, ids):
   for id in list(ids):
       click.echo(json.dumps(ctx.obj['emp'].get_results_by_contract(id, token, ot), indent=4))


if __name__ == '__main__':
    Ramman(obj={'config': config})
