from Bootstrap.ModulesBuilder.DeleteModuleBuilder import DeleteModuleBuilder
from Application.Presenters.ResultFormatter import ResultFormatter
from Bootstrap.ApplicationBuilder import ApplicationBuilder
from Bootstrap.ParserBuilder import ParserBuilder
from Presentation.CLI.Parsers.DeleteParser import DeleteParserBuilder
from Presentation.CLI.Request.RequestFactory import RequestFactory
from Presentation.CLI.Parsers.MoveParserBuilder import MoveParserBuilder
from Application.Move.MoveModuleBuilder import MoveModuleBuilder
from Application.Common.Result import CommandResult


def main() -> None:
    request_factory = RequestFactory()
    formatters: dict[type[CommandResult], ResultFormatter] = {}
    application = (
        ApplicationBuilder(request_factory, formatters)
        .add_command(DeleteModuleBuilder())
        .add_command(MoveModuleBuilder())
        .build()
    )
    parser = ParserBuilder().add(DeleteParserBuilder).add(MoveParserBuilder).build()
    
 

    
    application.run(parser.parse_args())


if __name__ == "__main__":
    main()
