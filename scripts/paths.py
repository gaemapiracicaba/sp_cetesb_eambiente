"""
Pastas do projeto
dez.22
"""

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

temp_path = data_path / 'temp'
temp_path.mkdir(exist_ok=True)

if __name__ == '__main__':
    print(project_path)
