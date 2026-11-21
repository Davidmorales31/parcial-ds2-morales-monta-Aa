"""creamos el main.py para hacer las consulta los tickets y muestra los resultados de la mesa de ayuda."""



import json
import os
from pathlib import Path
from pymongo import MongoClient
from moelo import MesaDeAyuda
