#!/usr/bin/python3
import sys
from loguru import logger
from pycolor_palette_loguru.logger import (
	PyDBG_Obj,
	set_default_theme,
	setup_logger,
)
from pycolor_palette_loguru.paint import (
	info_message,
	warn_message,
	error_message,
	other_message,
	debug_message,
	run_exception,
)
from pycolor_palette_loguru.pygments_colorschemes import CatppuccinMocha
from app import create_app

set_default_theme(CatppuccinMocha)
pydbg_obj = PyDBG_Obj()
setup_logger()


def main():
	app = create_app()

	if len(sys.argv) > 1:
		if sys.argv[1] == 'db':
			with app[0].app_context():
				app[1].create_all()

	app[0].run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
	main()

