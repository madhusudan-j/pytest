from flask import json, json, Response, flash
from flask import Flask, render_template, request, redirect, url_for
import os, re, subprocess
import xml.etree.ElementTree as ET
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

class MtcVersion:
    
    mtc_instal_path = r"C:\MTC10Tools"
    mtc_ver_path = r"C:\MTC10Base\MTCDB"
    def install_mtc(self, request, version, review):
        mtc_powershellPath = r"PowerShell C:\MTC10Base\MTCDB\installMTC.ps1"
        print("Running MTC phase...")
        if review == "install": 
            command = mtc_powershellPath + " -MTCVersion " + version # powershell "C:\MTC10Base\MTCDB\installMTC.ps1" -MTCVersion 10.5.1.0
        else:
            command = mtc_powershellPath + " -MTCVersion " + version + " -UnInstall" # powershell "C:\MTC10Base\MTCDB\installMTC.ps1" -MTCVersion 10.5.1.0 -UnInstall
        process = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE,universal_newlines=True)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output)
        rc = process.poll()
        print("*" * 10, rc)
        return redirect(request.referrer)

    def install_mtc_console_data(self, request):
        version = request.args.get('version')
        review = request.args.get('review')
        print(version, review, "###############################")
        def inner():
            mtc_powershellPath = r"PowerShell C:\MTC10Base\MTCDB\installMTC.ps1"
            print("Running MTC phase...")
            if review == "install": 
                command = mtc_powershellPath + " -MTCVersion " + version # powershell "C:\MTC10Base\MTCDB\installMTC.ps1" -MTCVersion 10.5.1.0
            else:
                command = mtc_powershellPath + " -MTCVersion " + version + " -UnInstall" # powershell "C:\MTC10Base\MTCDB\installMTC.ps1" -MTCVersion 10.5.1.0 -UnInstall
            process = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE,universal_newlines=True)
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(output)        
                    yield '%s<br/>\n' % output
        env = Environment(loader=FileSystemLoader('templates'))
        tmpl = env.get_template('mtc_versions.html') # to create flash model in same page. not yet done have some error 
        # tmpl = env.get_template('result.html') # it'll display console data in new webpage
        # return Response(tmpl.generate(result=inner()))
        return Response(inner(),  mimetype='application/json')
