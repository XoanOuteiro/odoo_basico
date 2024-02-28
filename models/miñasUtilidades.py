import locale
import os,platform

from odoo import models, api

def cadeaTextoSegunPlataforma(cadeaTextoWindows, cadeaTextoGNULinux):
    if platform.system().lower() == 'windows':
        cadeaTexto = cadeaTextoWindows
    else:
        cadeaTexto = cadeaTextoGNULinux
    return cadeaTexto




