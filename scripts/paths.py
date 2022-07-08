#!/usr/bin/env python
# coding: utf-8

from pathlib import Path

project_path = Path(__file__).parents[1].resolve()

scrapy_path = project_path / 'scrapy'
scrapy_path.mkdir(exist_ok=True)

driver_path = scrapy_path / 'driver'
driver_path.mkdir(exist_ok=True)

log_path = scrapy_path / 'logs'
log_path.mkdir(exist_ok=True)

adds_path = scrapy_path / 'adds'
adds_path.mkdir(exist_ok=True)

data_path = project_path / 'data'
data_path.mkdir(exist_ok=True)


if __name__ == '__main__':
    print(f'A pasta do projeto é: {project_path}')
    print(f'A pasta do scrapy é:  {scrapy_path}')
    print(f'A pasta do driver é:  {driver_path}')
    print(f'A pasta do log é:     {log_path}')
    print(f'A pasta do adds é:    {adds_path}')
