from flask import Flask, redirect, request
from flask.templating import render_template
from flask import Blueprint
from forms.EditKundenForm import editKundenForm
from forms.addAutoForm import AddKundenForm
from models.models import db, Kunden


Kunden_blueprint = Blueprint('kunden_blueprint', __name__)

@Kunden_blueprint.route("/Kunden.html", methods = ["get", "post"])
def Kunden_requests():
    AddKundenFormObject = AddKundenForm()
    kunden = db.session.query(Kunden).all()

    if AddKundenFormObject.validate_on_submit():
        print(AddKundenFormObject.KundenID.data)
        print(AddKundenFormObject.Vorname.data)
        print(AddKundenFormObject.Nachname.data)
        print(AddKundenFormObject.Geburtstag.data)
        print(AddKundenFormObject.Wohnohrt.data)
        print(AddKundenFormObject.Fuehrerscheinklasse.data)

        #hier in DB Speichern
        newKunden = Kunden()
        newKunden.KundenID = AddKundenFormObject.data
        newKunden.Vorname = AddKundenFormObject.Vorname.data
        newKunden.Nachname = AddKundenFormObject.Nachname.data
        newKunden.Geburtstag = AddKundenFormObject.Geburtstag.data
        newKunden.Wohnohrt = AddKundenFormObject.Wohnohrt.data
        newKunden.Fuehrerscheinklasse = AddKundenFormObject.Fuehrerscheinklasse.data

        db.session.add(newKunden)
        db.session.commit()


    return render_template("Kunden.html", \
        headline="Automarke", \
        form = AddKundenFormObject, \
        kunden = kunden)

def submitEditForm():
    editKundenFormObject = editKundenForm()

    if editKundenFormObject.validate_on_submit():
        
        KundenID = editKundenFormObject.Kunden.data
        Kunden_to_edit = db.session.query(Kunden).filter(Kunden.KundenID == KundenID).first()
        Kunden_to_edit.Vorname = editKundenFormObject.Vorname.data
        
        db.session.commit()

        return redirect("/")

    else:
        raise ("Fatal Error")

@Kunden_blueprint.route("/editKundenForm.py")
def showEditForm():
    KundenID = request.args["KundenID"]
    print(KundenID)
    
    Kunden_to_edit = db.session.query(Kunden).filter(Kunden.KundenID == KundenID).first()
    editKundenFormObject = editKundenForm()

    editKundenFormObject.KundenID.data =  Kunden_to_edit.KundenID
    editKundenFormObject.Vorname.data = Kunden_to_edit.Vorname
    editKundenFormObject.Nachname.data = Kunden_to_edit.Nachname
    editKundenFormObject.Geburtstag.data = Kunden_to_edit.Geburtstag
    editKundenFormObject.Wohnohrt.data = Kunden_to_edit.Wohnohrt
    editKundenFormObject.Fuehrerscheinklasse.data= Kunden_to_edit.Fuehrerscheinklasse
    


    return render_template("Kunden.html", form = editKundenForm)