import wikipedia
from wikibot import cli
from click.testing import CliRunner


def test_wikipage():
    runner = CliRunner()
    result = runner.invoke(cli, ["--name", "Facebook"])
    assert result.exit_code == 0
    assert "facebook" in result.output
