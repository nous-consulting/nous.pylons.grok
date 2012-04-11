"""Grokking utilites for pylons."""
import martian
import zope.configuration.config

from pylons import request, tmpl_context, response, session, translator, url, config
from pylons.i18n.translation import _get_translator


the_multi_grokker = martian.MetaMultiGrokker()
the_module_grokker = martian.ModuleGrokker(the_multi_grokker)


def skip_tests(name):
    return name in ['tests', 'ftests']


def grokDirective(_context, package):
    do_grok(package.__name__, _context)


def do_grok(dotted_name, config):
    martian.grok_dotted_name(
        dotted_name, the_module_grokker, exclude_filter=skip_tests,
        config=config
        )


def grok_app(conf, packages=None):
    if packages is None:
        packages = []

    items = [request, tmpl_context, response, session, url]
    translator._push_object(_get_translator(None))
    config._push_object(conf)

    for item in items:
        item._push_object(object())

    zope_config = zope.configuration.config.ConfigurationMachine()
    do_grok('grokcore.component', zope_config)
    for package in packages:
        do_grok(package, zope_config)
    zope_config.execute_actions()

    translator._pop_object()
    config._pop_object()
    for item in items:
        item._pop_object()

