from flet import *
from costom_check_box import CustomCheckBox
from calender import *
from babel.dates import format_date
from connector import *



def main(page: Page):



    BG = '#dbe0e1'
    BG1 = '#335e84'  #dark blue
    BG2 = '#85b014'  # vibrant green
    BG3 = '#a1c067'  # light green
    BG4 = '#6c8ca4'  # grayish blue
    BG5 = '#03223d'

    tdayf = datetime.date.today().strftime('%d-%m-%Y')

    def dropdown_changed00(e):
        t00.value = f" Bienvenue {dd00.value} "
        page.update()

    def dropdown_changed13(e):
        t13.value = f"Réaction Allérgique {dd13.value}"
        page.update()

    def dropdown_changed12(e):
        t12.value = f"Réaction Allérgique {dd12.value}"
        page.update()

    def dropdown_changed10(e):
        t10.value = f"Réaction Allérgique {dd10.value}"
        page.update()


    def dropdown_changed9(e):
        t9.value = f"Place de Lésions:  {dd9.value}"
        page.update()

    def dropdown_changed8(e):
        t8.value = f"Nombre de Lésions:  {dd8.value}"
        page.update()

    def dropdown_changed7(e):
        t7.value = f"Etat Origine de l'Animal:  {dd7.value}"
        page.update()

    def dropdown_changed6(e):
        t6.value = f"Etat de l'Animal:  {dd6.value}"
        page.update()

    def dropdown_changed5(e):
        t5.value = f"Profondeur :  {dd5.value}"
        page.update()

    def dropdown_changed4(e):
        t4.value = f"Produit :  {dd4.value}"
        page.update()

    def dropdown_changed3(e):
        t3.value = f"SEXE :  {dd3.value}"
        page.update()

    def dropdown_changed2(e):
        t2.value = f"Type de Contact Avec l'Animal : {dd2.value}"
        page.update()

    def dropdown_changed1(e):
        t1.value = f"NATIONALITE :  {dd1.value}"
        page.update()

    t00 = Text(value='Veuillez choisir l\'agent d\'inscription:',
        size=20, font_family='Georgia', italic=True, color='black'
    )
    dd00 = Dropdown(label='Agent d\'Inscription', border_color='#24415b',
                    on_change=dropdown_changed00,
                    padding=20,
                    icon=icons.PERSON_4,

                    bgcolor=colors.with_opacity(0.01,colors.WHITE),
                    label_style=TextStyle(
                        color=colors.BLUE_GREY_800

                    ),

                    options=[
                        dropdown.Option("Agent 1"),
                        dropdown.Option("Agent 2"),
                        dropdown.Option("Agent 3"),
                        dropdown.Option("Agent 4"),
                        dropdown.Option("Agent 5"),

                    ],
                    text_style=TextStyle(

                        weight= 'BOLD'
                    ),
                    color='BLACK',
                    width=300, )
    agent = Container(
        Column(controls=[
            t00,dd00,
        ]))

    t15= Text(
        color='WHITE',
        font_family='Georgia',
        size=20,
    )


    t14 = Text(
        color='BLACK',
        font_family='Georgia',
        size=20,
    )
    t13 = Text(
        color='BLACK',
        font_family='Georgia',
    )
    dd13 = Dropdown(label='Réaction Allergique Générale', border_color='#24415b',
                    on_change=dropdown_changed13,

                    label_style=TextStyle(
                        color=colors.BLUE_GREY_800
                    ),

                    options=[
                        dropdown.Option("OUI"),
                        dropdown.Option("NON"),
                    ],
                    color='RED',
                    width=200, )

    reaction_gen = Container(
        Row(controls=[
            dd13,
        ]))


    t12 = Text(
        color='BLACK',
        font_family='Georgia',
    )


    dd12 = Dropdown(label='Réaction Allergique Locale', border_color='#24415b',
                    on_change=dropdown_changed12,

                    label_style=TextStyle(
                        color=colors.BLUE_GREY_800
                    ),

                    options=[
                        dropdown.Option("OUI"),
                        dropdown.Option("NON"),
                    ],
                    color='RED',
                    width=200, )

    reaction_loc = Container(
        Row(controls=[
            dd12,
        ]))

    t11 = Text(
        color='BLACK',
        font_family='Georgia',
        size = 20

    )

    t10 = Text()
    dd10 = Dropdown(label='Réaction Allergique', border_color='#24415b',
                   on_change=dropdown_changed10,

                    label_style=TextStyle(
                        color=colors.BLUE_GREY_800
                    ),

               options=[
                       dropdown.Option("OUI"),
                       dropdown.Option("NON"),
                   ],
                    color = 'RED',
                   width=200, )

    reaction_aller = Container(
        Row(controls=[
            dd10,
        ]))


    t9 = Text()
    dd9 = Dropdown(label='Place de Lésions', border_color=BG3,
                   on_change=dropdown_changed9,
                   options=[
                       dropdown.Option("MAIN DROITE"),
                       dropdown.Option("MAIN GAUCHE"),
                       dropdown.Option("COU"),
                       dropdown.Option("TETE"),
                       dropdown.Option("PIED DROIT"),
                       dropdown.Option("PIED GAUCHE"),
                       dropdown.Option("OGE"),
                       dropdown.Option("CENTRE"),
                   ],
                   width=230, )

    place_lesion = Container(
        Row(controls=[
            dd9,
        ]))

    t8 = Text()
    dd8 = Dropdown(label='Nombre de Lésion', border_color=BG3,
                   on_change=dropdown_changed8,
                   options=[
                       dropdown.Option("UNIQUE"),
                       dropdown.Option("MULTIPLE"),
                   ],
                   width=230, )

    nb_lesion = Container(
        Row(controls=[
            dd8,
        ]))


    t7 = Text()
    dd7 = Dropdown(label='Etat Original de l\'Animal', border_color=BG3,
                   on_change=dropdown_changed7,
                   options=[
                       dropdown.Option("CONNU"),
                       dropdown.Option("ERRANT"),
                       dropdown.Option("DIVAGANT"),
                       dropdown.Option("MALADE"),
                   ],
                   width=230, )

    etat_ori_animal = Container(
        Row(controls=[
            dd7,
        ]))

    t6 = Text()
    dd6 = Dropdown(label='Etat de l\'Animal', border_color=BG3,
                   on_change=dropdown_changed6,
                   options=[
                       dropdown.Option("EN OBSERVATION"),
                       dropdown.Option("VIVANT"),
                       dropdown.Option("INCONNU"),
                       dropdown.Option("ABATTU"),
                       dropdown.Option("MORT"),
                       dropdown.Option("EN FUITE"),
                   ],
                   width=220, )

    etat_animal = Container(
        Row(controls=[
            dd6,
        ]))

    t5 = Text()
    dd5 = Dropdown(label='Profondeur de la Lésion', border_color=BG3,
                   on_change=dropdown_changed5,
                   options=[
                       dropdown.Option("TRES SUPERFICIELLE"),
                       dropdown.Option("SUPERFICIELLE"),
                       dropdown.Option("PEU PROFONDE"),
                       dropdown.Option("PROFONDE"),
                       dropdown.Option("TRES PROFONDE"),
                       dropdown.Option("CONTACT"),
                       dropdown.Option("LECHAGE"),
                   ],
                   width=300, )

    profondeur_patient = Container(
        Row(controls=[
            dd5,
        ]))

    t4 = Text()
    dd4 = Dropdown(label='Produit Utilisé Sur la Lésion', border_color=BG3,
                   on_change=dropdown_changed4,
                   options=[
                       dropdown.Option("SAVON"),
                       dropdown.Option("DERIVES IODES"),
                       dropdown.Option("DAKIN"),
                       dropdown.Option("ALCOOL"),
                       dropdown.Option("AUTRE"),
                       dropdown.Option("EAU DE JAVEL"),
                       dropdown.Option("SAVON ET ALCOOL"),
                       dropdown.Option("SAVON + DAKIN"),
                       dropdown.Option("SAVON + DERIVES IODES"),
                       dropdown.Option("DAKIN + DERIVES IODES"),
                   ],
                   width=300, )

    produit_patient = Container(
        Row(controls=[
            dd4,
        ]
        ))


    t3 = Text()
    dd3 = Dropdown(label='Sexe du Patient', border_color=BG3,
                   on_change=dropdown_changed3,
                   options=[
                       dropdown.Option("FEMININ"),
                       dropdown.Option("MASCULIN"),
                   ],
                   width=300, )

    sexe_patient = Container(
        Row(controls=[
            dd3,
        ]
        ))




    t2 = Text()
    dd2 = Dropdown(label='Type de Contact Avec l\'Animal', border_color=BG3,
                   on_change=dropdown_changed2,
                   options=[
                       dropdown.Option("MORSURE"),
                       dropdown.Option("GRIFFURE"),
                       dropdown.Option("MORSURE ET GRIFFURE"),
                       dropdown.Option("CONTACT"),
                       dropdown.Option("LECHAGE"),

                   ],
                   width=300, )
    contact_anim = Container(
        Row(controls=[
            dd2,
        ]
        ))


    t1 = Text()
    dd1 = Dropdown(label='Nationalité du Patient', border_color=BG3,
                  on_change=dropdown_changed1,
                  options=[
                      dropdown.Option("TUNISIENNE"),
                      dropdown.Option("ETRANGERE"),

                  ],
                  width=220, )
    nation = Container(
        Row(controls=[
            dd1,

            ]
        ))

    def dropdown_changed(e):
        t.value = f"L'animal:  {dd.value}"
        page.update()


    t = Text()
    dd = Dropdown(label='Type d\'Animal',border_color=BG3,
        on_change=dropdown_changed,
        options=[
            dropdown.Option("Chat"),
            dropdown.Option("Chien"),
            dropdown.Option("Rat"),
            dropdown.Option("Mouton"),
            dropdown.Option("Mulet"),
            dropdown.Option("Ane"),
            dropdown.Option("Chèvre"),
            dropdown.Option("Porc"),
            dropdown.Option("Humain"),
            dropdown.Option("Renard"),
            dropdown.Option("Chauve-souris"),
            dropdown.Option("mouffette"),
            dropdown.Option("raton-laveur"),
            dropdown.Option("mouffette"),
            dropdown.Option("mouffette"),
        ],
        width=150,)
    type_anim = Container(
        Row(controls=[
            dd,
            ]
            ))


    val_date = Text(
        size=17,
        color="WHITE100",
        font_family='Times New Roman',
                     )

    def date_change(e):
        date_value = e.control.value
        formatted_date = format_date(
            date_value,
            format="full",
            locale="fr",)
        val_date.value = formatted_date
        page.update()

    date_input = DatePicker(on_change=date_change)  #overlay on the page
    page.overlay.append(date_input)

    calend = Container(
        Column(
            controls=[
                ElevatedButton("Date De La Morsure",
                               icon=icons.CALENDAR_TODAY,
                               color='WHITE',
                               bgcolor='#80ab12',
                               elevation=15,
                               style=ft.ButtonStyle(
                                   shape=RoundedRectangleBorder(radius=10),
                                   elevation={
                                       ControlState.DEFAULT: 15,
                                       ControlState.HOVERED: 5,
                                   },

                                   bgcolor={
                                       ControlState.HOVERED: colors.GREEN_900,
                                       ControlState.DEFAULT: colors.LIGHT_GREEN_600

                                   },
                                   color={
                                       ControlState.HOVERED: colors.WHITE,
                                       ControlState.FOCUSED: colors.BLUE,
                                       ControlState.DEFAULT: colors.BLACK,
                                   },

                               ),
                               on_click=lambda _:date_input.pick_date()),

                 val_date
            ]
    ),
    )

    def on_text_changenum(event):
        print(event.data)

    filter = InputFilter('^[0-9]*')

#BOUTTON DE SEROTHERAPIE:

    def button_clicked1(e):

        # type de sérum disponible
        list_SAR = ["equirab", "gamma-rab"]
        SAR = ""
        r = {}
        x = getSerum()
        for i in x:
            print(i)
        r = i
        SAR = r["type_serum"]
        dose_id = r["numero_lot"]
        print(SAR)
        print(dose_id)



        if SAR == "equirab":
            if int(poid_pat.value) < 75:
                dose = float(poid_pat.value) / 5
                dose = round(dose, 2)
                print("la dose totale du SAR est:", dose, "ml")
            else:
                dose = 15
                dose = round(dose, 2)
                print("la dose totale du SAR est:", dose, "ml")
        elif SAR == "gamma-rab":
            if int(poid_pat.value) < 90:
                dose = float(poid_pat.value) / 5
                dose = round(dose, 2)
                print("la dose totale du SAR est:", dose, "ml")
            else:
                dose = 30
                dose = round(dose, 2)
                print("la dose totale du SAR est:", dose, "ml")

        taille_papule = float(papule_taille.value)
        rougeur_autour = float(rougeur_taille.value)
        reaction = dd10.value
        if (taille_papule < 10 and rougeur_autour < 2.5 and reaction == "NON"):
            t11.value = (
                "Passer au Deuxième Test:\n0.25ml de SAR Sous-Cutanée\nAprès 15mn de l'Infiltration de Sérum:")
            # deuxième partie du test besredka
            reaction_local = dd12.value
            reaction_generale = dd13.value
            if (((reaction_local == "NON") == True) and ((reaction_generale == "NON") == True)):
                dose = dose - 0.35
                dose = round(dose, 2)
                out = ("Test Besredka Négatif!\nLa dose de sérum à administrer le  "+ str(tdayf)+" est "+str(dose)+" ml\n"+
                       "Sérum à utiliser: "+SAR)
                t14.value = out
        else:
            t11.value = ("ATTENTION! Patient Allergique Au SAR! ")




        page.update()


#BOUTTON D'ENREGISTREMENT :
    def button_clicked(e):
        # Update text field values and refresh the page
        txt.value = (
            f"Textboxes values are: '{cd.value}','{numcin.value}',  '{nom.value}', '{prenom.value}', '{nomp.value}', '{dateins.value}','{numtel.value}'."
        )

        insertPatient(numcin.value, nom.value, prenom.value, numtel.value)

        # ---------------------------------------------------CODE-----------------------------------------------------
        format = '%Y-%m-%d'

        # Current date

        tday = datetime.date.today()
        tdelta3 = datetime.timedelta(days=3)
        tdelta7 = datetime.timedelta(days=7)
        tdelta14 = datetime.timedelta(days=14)
        tdelta21 = datetime.timedelta(days=21)
        tdelta28 = datetime.timedelta(days=28)
        tdelta90 = datetime.timedelta(days=90)

        # print(tday - tdelta7 )

        # input Ptients Data
        # firstname_lastname
        # inserting the data of the Patient in the db

        local = 0
        glob = 0
        cin = numcin.value
        # etat de l'animal
        etat = ""
        if dd6.value == "EN OBSERVATION" or dd6.value == "VIVANT":
            etat = "observable"
        else:
            etat = "non observable"

        # nombre de lésion
        nombre = dd8.value
        print(nombre)
        # profondeur de la lésion

        profondeur = ""
        if dd5.value == "PEU PROFONDE" or dd5.value == "PROFONDE" or dd5.value == "TRES PROFONDE":
            profondeur = "profonde"
        else:
            profondeur = "superficielle"

        siege = dd9.value
        # siège de la lésion
        list_extremite = ["MAIN DROITE", "MAIN GAUCHE", "COU", "TETE", "PIED DROITE", "PIED GAUCHE", "OGE"]

        # condition pour faire serum
        test = 0
        if etat == "observable":
            if (profondeur == "pronfonde" and (nombre == "MULTIPLE") or siege in list_extremite):
                test = 1
        elif etat == "non observable":
            if (profondeur == "pronfonde" or (nombre == "MULTIPLE" or nombre == "UNIQUE") or siege in list_extremite):
                test = 1

        # type de sérum disponible
        list_SAR = ["equirab", "gamma-rab"]
        SAR = ""
        r = {}
        x = getSerum()
        for i in x:
            print(i)
        r = i
        SAR = r["type_serum"]
        dose_id = r["numero_lot"]
        print(SAR)
        print(dose_id)


        if test == 1:
            # ----------------------------------------------------------------------------------------------------------
            # les conditions de sérothérapie
            # test sur le type du sérum antirabique disponible(à transformer sur le tableau)
            if SAR == "equirab":
                if int(poid_pat.value) < 75:
                    dose = float(poid_pat.value) / 5
                    dose = round(dose, 2)
                    print("la dose totale du SAR est:", dose, "ml")
                else:
                    dose = 15
                    dose = round(dose, 2)
                    print("la dose totale du SAR est:", dose, "ml")
            elif SAR == "gamma-rab":
                if int(poid_pat.value) < 90:
                    dose = float(poid_pat.value) / 5
                    dose = round(dose, 2)
                    print("la dose totale du SAR est:", dose, "ml")
                else:
                    dose = 30
                    dose = round(dose, 2)
                    print("la dose totale du SAR est:", dose, "ml")

            # ------------------------------------------------------------------------------------------------------------------------------------
            # test besredka
            # première partie
            # input taille papule , rougeur_autour, réaction
            taille_papule = float(papule_taille.value)
            rougeur_autour = float(rougeur_taille.value)
            reaction = dd10.value
            if (taille_papule < 10 and rougeur_autour < 2.5 and reaction == "non"):
                # deuxième partie du test besredka
                reaction_local = dd12.value
                reaction_generale = dd13.value
                if (((reaction_local == "NON") == True) and ((reaction_generale == "NON") == True)):
                    dose = dose - 0.35
                    dose = round(dose, 2)

      # get from vaccin
        v = {}
        x = getVaccins()
        for i in x:
            print(i)
        v = i

        # ------------------------------------------------------------------------------------------------------------------
        # les conditions de vaccination

        if etat == "observable":
            if test == 0:
                ftxt = ("Protocole ZAGREB A2\nVos dates de vaccin seront  :\n2 dose de vaccin le: " + str(tday) +
                        "\nvos prochains rendez-vous seront  :\n1 dose de vaccin le:  " + str(tday + tdelta7) +
                        " (Si l'animal est mort ou en fuite après déclaration)")

                t15.value = ftxt
                # Insertion into MySQL database

                r1 = tday.strftime('%Y-%m-%d')
                r3 = (tday + tdelta7).strftime('%Y-%m-%d')
                r4 = (tday + tdelta14).strftime('%Y-%m-%d')
                r5 = (tday + tdelta28).strftime('%Y-%m-%d')

                insertVaccination(r1, v["numero_lot"], 2, cin)
                insertVaccination(r3, v["numero_lot"], 1, cin)

                # Update Vaccin
                nbvacc = v["quantite"] - 2
                nb = v["numero_lot"]
                if nb >= 10:
                    print(nbvacc)
                    updateVaccin(nb, v["dlc_vaccin"], nb, nbvacc)
                else:
                    print("Quantite de vaccin insuffisate!")

            else:

                ftxt = ("Protocole ESSEN A1\nUne Dose de Sérum le: " + str(tday) + "\net Une Dose de Vaccin le: " + str(tday) +
                        "\nVos prochains rendez-vous seront  :\n1 dose de vaccin le:  " + str(tday + tdelta3) +
                        "\n1 dose de vaccin le:  " + str(tday + tdelta7) +
                        " (Si l'animal est mort ou en fuite après déclaration)")

                t15.value = ftxt

                # insertion db
                r1 = tday.strftime('%Y-%m-%d')
                r2 = (tday + tdelta3).strftime('%Y-%m-%d')
                r3 = (tday + tdelta7).strftime('%Y-%m-%d')
                r4 = (tday + tdelta14).strftime('%Y-%m-%d')
                r5 = (tday + tdelta28).strftime('%Y-%m-%d')

                if test == 1:
                    # Construct the dictionary
                    s = {
                        "dose_id": dose_id,
                        "dose_total": dose,
                        "date_administration": r1,
                        "quantite_local": local,
                        "quantite_generale": glob,
                        "patient_id": cin,
                        "numero_lot": dose_id
                    }

                    # Call the insertion function
                    insertSerotherapie(s["dose_id"], s["dose_total"], s["date_administration"], s["quantite_local"],
                                       s["quantite_generale"], s["patient_id"], s["numero_lot"])

                insertVaccination(r1, v["numero_lot"], 1, cin)
                insertVaccination(r2, v["numero_lot"], 1, cin)
                insertVaccination(r3, v["numero_lot"], 1, cin)

                # Update Vaccin
                nbvacc = v["quantite"] - 3
                nb = v["numero_lot"]
                if nb >= 10:
                    print(nbvacc)
                    updateVaccin(nb, v["dlc_vaccin"], nb, nbvacc)
                else:
                    print("Quantite de vaccin insuffisate!")

                # Update Serum
                nbser = r["quantite"] - 1
                nbs = r["numero_lot"]
                typeser = r["type_serum"]
                if nbs >= 5:
                    print(nbser)
                    updateSerum(nbs, v["dlc_vaccin"], nbs, nbser, typeser)
                else:
                    print("Quatite de serum insuffisate!")

        elif etat == "non observable":
            if test == 0:

                ftxt = ("Protocole ZAGREB B2\nVos Dates de Vaccin Seront:\n2 Doses de Vaccin le :" + str(tday) +
                        "\nVos prochains rendez-vous seront :\n1 dose de vaccin le:  " + str(tday + tdelta7) +
                        "\n1 dose de vaccin le:  " + str(tday + tdelta21) +
                        "\n1 dose de vaccin le:  " + str(tday + tdelta90))

                t15.value = ftxt
                # insertion db
                r1 = tday.strftime('%Y-%m-%d')
                r2 = (tday + tdelta7).strftime('%Y-%m-%d')
                r3 = (tday + tdelta21).strftime('%Y-%m-%d')
                r4 = (tday + tdelta90).strftime('%Y-%m-%d')

                insertVaccination(r1, v["numero_lot"], 2, cin)
                insertVaccination(r2, v["numero_lot"], 1, cin)
                insertVaccination(r3, v["numero_lot"], 1, cin)
                insertVaccination(r4, v["numero_lot"], 1, cin)

                # Update Vaccin
                nbvacc = v["quantite"] - 5
                nb = v["numero_lot"]
                if nb >= 10:
                    print(nbvacc)
                    updateVaccin(nb, v["dlc_vaccin"], nb, nbvacc)
                else:
                    print("Quatite de vaccin insuffisate!")


            else:

                ftxt = ("Protocole ESSEN B1\nUne Dose de Sérum le:" + str(tday) + "\net Une Dose de Vaccin le: " + str(tday) +
                        "\nVos prochains rendez-vous seront:\n1 dose de vaccin le:  " + str(tday + tdelta3) +
                        "\n1 dose de vaccin le:  " + str(tday + tdelta7) +
                        "\n1 dose de vaccin le:  " + str(tday + tdelta14) +
                        "\n1 dose de vaccin le:  " + str(tday + tdelta28) +
                        "\n1 dose de vaccin le:  " + str(tday + tdelta90)

                        )

                t15.value = ftxt
                # insertion db
                r1 = tday.strftime('%Y-%m-%d')
                r2 = (tday + tdelta3).strftime('%Y-%m-%d')
                r3 = (tday + tdelta7).strftime('%Y-%m-%d')
                r4 = (tday + tdelta14).strftime('%Y-%m-%d')
                r5 = (tday + tdelta28).strftime('%Y-%m-%d')
                r6 = (tday + tdelta90).strftime('%Y-%m-%d')

                # Construct the dictionary
                s = {
                    "dose_id": dose_id,
                    "dose_total": dose,
                    "date_administration": r1,
                    "quantite_local": local,
                    "quantite_generale": glob,
                    "patient_id": cin,
                    "numero_lot": dose_id
                }

                # Call the insertion function
                insertSerotherapie(s["dose_id"], s["dose_total"], s["date_administration"], s["quantite_local"],
                                   s["quantite_generale"], s["patient_id"], s["numero_lot"])

                insertVaccination(r1, v["numero_lot"], 1, cin)
                insertVaccination(r2, v["numero_lot"], 1, cin)
                insertVaccination(r3, v["numero_lot"], 1, cin)
                insertVaccination(r4, v["numero_lot"], 1, cin)
                insertVaccination(r5, v["numero_lot"], 1, cin)
                insertVaccination(r6, v["numero_lot"], 1, cin)

                # Update Vaccin
                nbvacc = v["quantite"] - 5
                nb = v["numero_lot"]
                if nb >= 10:
                    print(nbvacc)
                    updateVaccin(nb, v["dlc_vaccin"], nb, nbvacc)
                else:
                    print("Quatite de vaccin insuffisate!")

                # Update Serum
                nbser = r["quantite"] - 1
                nbs = r["numero_lot"]
                typeser = r["type_serum"]
                if nbs >= 5:
                    print(nbser)
                    updateSerum(nbs, v["dlc_vaccin"], nbs, nbser, typeser)
                else:
                    print("Quatite de serum insuffisate!")





        nom.value = ""
        numcin.value = ""
        prenom.value = ""
        nomp.value = ""
        numtel.value = ""
        age_pat.value = ""
        poid_pat.value = ""
        papule_taille.value = ""
        rougeur_taille.value = ""
        etat_animal.value = ""
        etat_ori_animal.value = ""
        dd1.value = ""
        dd2.value = ""
        dd3.value = ""
        dd4.value = ""
        dd5.value = ""
        dd6.value = ""
        dd7.value = ""
        dd8.value = ""
        dd9.value = ""
        dd10.value = ""
        dd13.value = ""
        dd12.value = ""





        page.update()


    # Create a text element for displaying results
    txt = Text()

    # Define text fields
    cd = TextField(label="Code", read_only=True, value="85024", border_color=BG3,color="WHITE300")
    nom = TextField(label="Nom du Patient",
                    capitalization=TextCapitalization.WORDS,
                    cursor_color=BG3, border_color=BG3,
                    color="WHITE300",
                    autofocus=True,)
    prenom = TextField(label="Prénom du Patient",
                       capitalization=TextCapitalization.WORDS,
                       cursor_color=BG3, border_color=BG3,
                       color="WHITE300")
    nomp = TextField(label="Prénom du Père",
                     capitalization=TextCapitalization.WORDS,
                     cursor_color=BG3, border_color=BG3,

                     color="WHITE300")

    dateins = TextField(label="Date d'Inscription",
                        value=tdayf,
                        cursor_color=BG3, border_color=BG3,
                        color="WHITE300",
                        read_only=True)

    numtel = TextField(label="Numero de Téléphone",
                        input_filter=filter, on_change=on_text_changenum,
                        cursor_color=BG3, border_color=BG3,
                        max_length=8,
                        color="WHITE300"
                    )

    numcin = TextField(label="Numéro de CIN du Patient",
                       input_filter=filter, on_change=on_text_changenum,
                       cursor_color=BG3, border_color=BG3,
                       max_length=8,
                       color="WHITE300"
                       )

    age_pat = TextField(label="Age du Patient",
                       input_filter=filter, on_change=on_text_changenum,
                       cursor_color=BG3, border_color=BG3,
                        suffix_text='ans',
                       max_length=2,
                       color="WHITE300"
                       )

    poid_pat = TextField(label="Poids du Patient",
                        input_filter=filter, on_change=on_text_changenum,
                        cursor_color=BG3, border_color=BG3,
                        suffix_text='kg',
                        max_length=3,

                        color="WHITE300"
                        )
    papule_taille = TextField(label="Taille de la Papule",
                         width=350,
                         input_filter=filter, on_change=on_text_changenum,
                         cursor_color='#24415b', border_color='#24415b',
                         label_style=TextStyle(
                                  color=colors.BLUE_GREY_800
                              ),
                         suffix_style=TextStyle(
                                  color=colors.BLUE_GREY_800
                              ),

                         suffix_text='mm',
                         max_length=2,
                         color="BLACK",

                         )
    rougeur_taille = TextField(label="Taille de la Rougeur Autour de la Lésion",
                               width=350,
                               label_style=TextStyle(
                                   color=colors.BLUE_GREY_800
                               ),

                              input_filter=filter, on_change=on_text_changenum,
                              cursor_color='#24415b', border_color='#24415b',
                              suffix_text='cm',
                              suffix_style=TextStyle(
                                 color=colors.BLUE_GREY_800
                              ),
                              max_length=1,
                              color="BLACK",

                              )




# BOUTTON DE SEROTHERAPIE:
    bs = ElevatedButton("Test Besredka",
                       color='WHITE',
                       elevation=20,
                       icon=icons.MEDICAL_INFORMATION,
                       bgcolor='BLACK',
                       on_click=button_clicked1,

                       style=ft.ButtonStyle(
                           shape=RoundedRectangleBorder(radius=10),
                           elevation={
                               ControlState.DEFAULT: 15,
                               ControlState.HOVERED: 5,
                           },

                           bgcolor={
                               ControlState.HOVERED: colors.BLUE_GREY_900,
                               ControlState.DEFAULT: colors.BLUE_GREY_50,

                           },
                           color={
                               ControlState.HOVERED: colors.WHITE,
                               ControlState.FOCUSED: colors.BLUE,
                               ControlState.DEFAULT: colors.BLACK,
                           },

                       ),

                       )


# BOUTTON D'ENREGISTREMENT:
    b = ElevatedButton("Enregister",
                       color='BLACK',
                       elevation= 20,
                       icon=icons.SAVE,
                       bgcolor='WHITE',
                       on_click=button_clicked,

                       style=ft.ButtonStyle(
                           shape=RoundedRectangleBorder(radius=10),
                           elevation={
                               ControlState.DEFAULT: 15,
                               ControlState.HOVERED: 5,
                           },

                           bgcolor={
                               ControlState.HOVERED: colors.BLUE_GREY_800,
                               ControlState.DEFAULT: colors.WHITE,

                           },
                           color={
                               ControlState.HOVERED: colors.WHITE,
                               ControlState.FOCUSED: colors.BLUE,
                               ControlState.DEFAULT: colors.BLACK,
                           },

                       ),

                       )



    def restore(e):
        page_2.controls[0].width = 1453.5
        page_2.controls[0].scale = transform.Scale(
            1, alignment=alignment.center_right)
        page_2.update()

    def shrink(e):
        page_2.controls[0].width = 400
        page_2.controls[0].scale = transform.Scale(
            0.9,alignment=alignment.center_right)
        page_2.controls[0].border_radius = border_radius.only(
            top_left=25,
            top_right=0,
            bottom_left=25,
            bottom_right=0,
        )
        page_2.update()

    def restore1(e):
        create_task_view.controls[0].width = 1900
        create_task_view.controls[0].scale = transform.Scale(
            1, alignment=alignment.center_right)
        create_task_view.update()

    def shrink1(e):
        create_task_view.controls[0].width = 800
        create_task_view.controls[0].scale = transform.Scale(
            1, alignment=alignment.top_left)
        create_task_view.controls[0].border_radius = border_radius.only(
            top_left=15,
            top_right=15,
            bottom_left=15,
            bottom_right=15,
        )
        create_task_view.update()

    serothe =Container(
            width=1900,
            height=825,
            border_radius=20,
            gradient=RadialGradient(
                center=Alignment(-0.3,0),
                radius=1,
                colors=[
                    "#6f8a3f",  # Green
                    "WHITE",  # well...White
                ]),
        padding=padding.only(left=815, top=5),
        content= Column(width=1000,
            controls=[
                FloatingActionButton(
                    bgcolor='#24415b',
                    icon=icons.ARROW_RIGHT_ALT,
                    hover_elevation=5,
                    elevation=10,
                    scale=0.9,
                    on_click=lambda e: restore1(e)

                ),
                Text(value='PREMIERE PARTIE DU TEST BESREDKA',
                     color='BLACK',
                     weight='bold',
                     size=18,
                     font_family='Georgia'),


                Text(value='Injection de 0.1ml de SAR intradermique:',
                     color='BLACK',
                     size=18,
                     font_family='Georgia'),
                papule_taille,
                rougeur_taille,
                reaction_aller,
                bs,t11,reaction_loc,reaction_gen,t14



            ]
        )

                        )


    create_task_view = Row(controls=[Container(
        animate=animation.Animation(800, AnimationCurve.EASE),
        animate_scale=animation.Animation(1000, AnimationCurve.DECELERATE),
        width=1900,
        height=825,
        gradient=LinearGradient(
                    begin=alignment.top_right,
                    end=alignment.bottom_left,
                    colors=['#0f1a24','#1d3449',"#24415b",'#1d3449','#0f1a24']),
        bgcolor=BG1,
        border_radius=25,
        padding=padding.only(left=10, top=20, right=200),



        content=Column(
            controls=[Row( spacing= 1180,
                controls=[
                    Container(
                        on_click=lambda _: page.go('/'), alignment = alignment.center,
                          height=50, width=50, content=Text("x",size=30)),
                    Row(spacing= 10,
                        controls=[
                            Container(
                                b
                            ),

                                 Row(
                                controls=[Container(
                                    Image(src='image.png'),
                                    width= 50,
                                )
                                ]),
                        ])

                        ]),
                    Row(
                        controls=[Container(
                            Text(value='Enregistrement d\' un nouveau Patient:',
                                           color='White',
                                           font_family='Georgia',
                                           italic=True,
                                           weight=FontWeight.BOLD,
                                           size=20),

                        )]
                    ),
                    Row(spacing=50,controls=[
                    Container(width=300 ,

                              content=Column(spacing=25,controls=[
                                cd,nom,prenom,nomp,numtel,numcin,dateins,nation,t1
                                 ])

                              ),
                    Row(spacing= 50,controls=[
                      Container(width=300, content=Column(spacing=10,controls=[
                          age_pat,poid_pat,sexe_patient,t3,contact_anim,t2,place_lesion,nb_lesion,profondeur_patient,t5,
                          produit_patient,t4,
                      ])),
                        Row(controls=[
                      Container(width=300, content=Column(spacing=25,controls=[
                          calend,type_anim,t,etat_animal,t6,etat_ori_animal,t7,txt,
                          ElevatedButton(
                              text='Test d\'Hypersensibilité Au Sérum',
                              icon=icons.MEDICATION,
                              bgcolor=BG3,
                              elevation=10,
                              style=ft.ButtonStyle(
                                  shape=RoundedRectangleBorder(radius=10),
                                  elevation={
                                      ControlState.DEFAULT: 15,
                                      ControlState.HOVERED: 5,
                                  },

                                  bgcolor={
                                      ControlState.HOVERED: colors.GREEN_900,
                                      ControlState.DEFAULT: colors.LIGHT_GREEN_600


                                  },
                                  color={
                                      ControlState.HOVERED: colors.WHITE,
                                      ControlState.FOCUSED: colors.BLUE,
                                      ControlState.DEFAULT: colors.BLACK,
                                  },

                              ),
                              on_click=lambda e: shrink1(e))
                      ])),
                            Row(controls=[
                                t15

                                ])


                        ])
                                    ]),
                    ]
        ),
                      ]

           ),
    )])


    tasks = Column(
        height=400,
        scroll='auto',
        #controls=[Container(height=20, width=900,bgcolor='red')]

    )

    for i in range(10):
        tasks.controls.append(
            Container(height=100, width=1500, bgcolor=BG5,border_radius=25,padding=padding.only (left=20,top=25,),
                      content=CustomCheckBox('green',
                      'MISE A JOUR NON DISPONIBLE ')
                      )),

    categories_card = Row(spacing=30,
                          scroll='auto'
                          )
    categories = ['Patient', 'Rendez-vous', 'Vaccination', 'Serotherapie', 'Utilisateur','Vaccins']
    for i, c in enumerate(categories):
        categories_card.controls.append(
            Container(
                bgcolor=BG, height=100, width=200, padding=10, border_radius=15, shadow=
                BoxShadow(
                spread_radius=2,
                blur_radius=15,
                color=colors.BLUE_GREY_300,
                offset=Offset(0, 0),
                blur_style=ShadowBlurStyle.OUTER,
    ) ,
                content=Column(
                    controls=[
                        Text(value='Enregistrer:', color='black', size=15),
                        Row(alignment='center',
                            controls=[
                                Container(Text(value=c, color='black', font_family='Georgia', size=15)),
                            FloatingActionButton(icon=icons.ADD, on_click=lambda _: page.go('/create_task'))
                            ]
                           )]
                )
        ))

    first_page_contents = Container(  #main page
        content=Column(
            controls=[
                Row(spacing=1325,
                    controls=[
                        Container(on_click = lambda e: shrink(e),scale = 1.5,
                            content=Icon(icons.MENU, color='black')),
                        Row(
                            controls=[Container(scale=1.5,
                                content=Icon(icons.SEARCH, color='black')),
                                Container(scale=1.5,
                                content=Icon(icons.SETTINGS, color='black')),
                            ]
                        )
                    ]
                    ),
                #Container(height=10),
                Text(value= "Bienvenue" , size=30, font_family='Georgia', italic=True, color='black'),
                Text(value='CATEGORIES', color='black'),
                Container(padding=padding.only(top=10, bottom=20), content=categories_card),
                Text(value='Mise à jour:', size=30, font_family='Georgia', italic=True, color='black'),
                Text(value='CATEGORIES', color='black'),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(bottom=100,right=20,
                            icon=icons.ADD, on_click=lambda _: page.go('/create_task'))
                    ]
                )
            ],
        ),
    )

    page_1 = Container(
        width=1453.5,
        height=825,
        bgcolor=BG,
        border_radius=25,
        padding=padding.only(left=10, top=20,right=200),

        content=Column(
            controls=[Row(alignment='start',
                controls=[
                Container(border_radius=25, padding=padding.only(left=13, top=5), height=50, width=50,
                          border=border.all(2,'black'),
                          on_click=lambda e: restore(e),
                    content=Text('<',color='black',size=25))]

                        ),
                      Container(
                          Row(controls=[
                          Image(src='images.png'),
                        Stack(controls=[
                          Text(
                              ),
                               Text(value="Institut Pasteur de Tunis",
                                    style=TextStyle(
                                        color="#a1c067",
                                        size=40,
                                        weight=FontWeight.BOLD,
                                        italic=True,
                                        font_family="Georgia",
                                        letter_spacing=2
                                    )

                          ),]),
                              ]), ),
                      Container(Column(
                          controls=[
                              agent,
                              
                              Text(value = "DESCRIPTION"
                                   , size=20, font_family='Georgia', color='black',weight='bold',italic=True),
                              
                              Text(value="Cette application de gestion du système de vaccination antirabique est conçue pour faciliter\nla gestion des protocoles de vaccination et le suivi des patients.\nElle permet aux professionnels de santé d'enregistrer les informations des patients,\nde gérer les calendriers de vaccination, et de suivre l'historique des vaccinations administrées.\nDe plus, l'application intègre une fonctionnalité qui prévoit et calcule la quantité\nde sérum antirabique à administrer en fonction des lésions identifiées,\nassurant ainsi une prise en charge optimale des patients.\nLe tout est soutenu par une base de données MySQL sécurisée et une interface utilisateur\nintuitive développée avec Flet pour une navigation fluide." 
                                
                                   
                                   , size=20, font_family='Georgia', color='black')
                          ]
                      )

                      )

                     ]

        ))
    page_2 = Row(alignment='end',     #main page
        controls=[
            Container(
                width=1453.5,
                height=825,
                gradient=LinearGradient(
                    begin=alignment.top_left,
                    end=alignment.bottom_right,
                    colors=['white',BG4,'#67b19f']),
                border_radius=25,
                animate=animation.Animation(600,AnimationCurve.EASE_IN_OUT_BACK),
                animate_scale=animation.Animation(400,AnimationCurve.DECELERATE),
                padding=padding.only(
                    top=50, left=20, right=20, bottom=5,
                ),
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )

    info = Container(
        content=
        Stack(controls=[
            serothe,
         create_task_view,
        ])
        )

    container = Container(
        width=1453.5,
        height=825,
        bgcolor=BG,
        border_radius=25,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        ))


    pages = {
        '/': View(
             "/",
            [
                        container
                    ],
                ),
        '/create_task': View(
            "/create_task",
            [
                        info
                    ],
                ),

    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )
        page.add(container)


    #page.window_title_bar_hidden = True
    #page.window_frameless = True
    #page.window_title_bar_buttons_hidden = True
    #page.bgcolor = colors.TRANSPARENT
    #page.window_bgcolor = colors.TRANSPARENT
    #page.window_width = 1400
    #page.window_height =1000

    page.on_route_change = route_change
    page.go(page.route)

#---------------------------------------------------CODE-----------------------------------------------------
   


#---------------------------------------------------NO MORE CODE---------------------------------------------


app(target=main)
