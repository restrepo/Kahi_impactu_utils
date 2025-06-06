

def ciarp_mapping(ror_code, entity):
    """
    Function to map ROR codes to categories based on a specific entity type.

    This function filters categories associated with a ROR code based on the
    specified entity type (e.g., "works", "patents", "events", "misc").

    Parameters:
    -----------
    ror_code : str
        The ROR code representing an institution. It must exist in the predefined mappings.
    entity : str
        The category type to filter by. It must be one of the following:
        "works", "patents", "events", "misc".

    Returns:
    --------
    list
        A list of category names associated with the provided ROR code and entity type.

    ------
    """
    ciarp_data_types = {
        "https://ror.org/03bp5hc83": {
            "Articulo corto publicado en libro de texto": "works",
            "Articulo corto publicado en libro resultado de investigacion": "works",
            "Articulo corto publicado en revista Tipo A1": "works",
            "Articulo corto publicado en revista Tipo A2": "works",
            "Articulo corto publicado en revista Tipo B1": "works",
            "Articulo corto publicado en revista Tipo C1": "works",
            "Articulo en revista de difusion internacional. Categoria A": "works",
            "Articulo en revista nacional de difusion local": "works",
            "Articulo en revista nacional de difusion nacional": "works",
            "Articulo en revista Tipo A1": "works",
            "Articulo en revista Tipo A2": "works",
            "Articulo en revista Tipo B": "works",
            "Articulo en revista Tipo B2": "works",
            "Articulo en revista Tipo C": "works",
            "Articulos nacionales publicados ante del 28/03/2003": "works",
            "Capitulo de libro de ensayo": "works",
            "Capitulo de libro de texto": "works",
            "Capitulo de libro resultado de investigacion": "works",
            "Capitulo de libro Tipo B": "works",
            "Capitulo de obra artistica": "works",
            "Capitulo de obra artistica nacional": "works",
            "Carta al editor en revista tipo A1": "works",
            "Carta al editor en revista tipo A2": "works",
            "Carta al editor en revista tipo B": "works",
            "Carta al editor en revista tipo C": "works",
            "Composicion musica de camara nacional": "misc",
            "Composicion musical musica de camara": "misc",
            "Comunicacion corta en revista Tipo A1": "works",
            "Comunicacion corta en revista Tipo A2": "works",
            "Comunicacion corta en revista Tipo B": "works",
            "Comunicacion corta en revista Tipo C": "works",
            "Cuento o relato de difusion nacional": "works",
            "Direccion de trabajo de grado de doctorado": "misc",
            "Direccion de trabajo de grado de especializacion medica()": "misc",
            "Direccion de trabajo de grado de maestria": "misc",
            "Director de actores en obra de teatro": "misc",
            "Editorial en revista tipo A1": "works",
            "Editorial en revista tipo A2": "works",
            "Editorial en revista tipo B": "works",
            "Editorial en revista tipo C": "works",
            "Estidio posdoctoral": "misc",
            "Impreso universitario": "works",
            "Interpretacion de impacto internacional": "misc",
            "Interpretacion de impacto local": "misc",
            "Interpretacion de impacto nacional": "misc",
            "Libro de ensayo": "works",
            "Libro de ensayo por capitulos": "works",
            "Libro de investigacion por capitulos resolucion 01 14/03/2018": "works",
            "Libro de literatura categoria A": "works",
            "Libro de texto": "works",
            "Libro de texto por capitulos": "works",
            "Libro resultado de investigacion": "works",
            "Libro resultado de investigacion por capitulos": "works",
            "Libro resultado de tesis doctoral categoria A": "works",
            "Libro resultado de tesis doctoral categoria B": "works",
            "Obra de creacion complementaria internacional.": "misc",
            "Obra de creacion complementaria o de apoyo local": "misc",
            "Obra de creacion complementaria o de apoyo Nacional": "misc",
            "Obra de creacion original artistica internacional": "misc",
            "Obra de creacion original artistica local": "misc",
            "Obra de creacion original artistica nacional": "misc",
            "PATENTE A4 VIA TRADICIONAL SIN PRODUCTO Y SIN CONTRATO": "patents",
            "PATENTE DE INVENCION": "patents",
            "Patente. Categoria A": "patents",
            "Ponencia de extension intermedia en evento internacional ()": "events",
            "Ponencia de extension intermedia en evento nacional ()": "events",
            "Ponencia de extension intermedia latinoameric o de 1 cont ()": "events",
            "Ponencia en extenso en evento iberoamericano ()": "events",
            "Ponencia en extenso en evento internacional": "events",
            "Ponencia en extenso en evento latinoamericano ()": "events",
            "Ponencia en extenso en evento local": "events",
            "Ponencia en extenso en evento nacional": "events",
            "Premio internacional": "misc",
            "Premio Internacional  C": "misc",
            "Premio internacional B": "misc",
            "Premio internacional D": "misc",
            "Premio nacional": "misc",
            "Premio nacional B": "misc",
            "Premio nacional C": "misc",
            "Premio nacional D": "misc",
            "Produccion Academica Especial": "misc",
            "Produccion especial para bonificacion": "misc",
            "Produccion fonografica didiactica local": "misc",
            "Produccion fonografica documental local": "misc",
            "Produccion fonografica nacional": "misc",
            "Produccion radiografica de difusion local": "misc",
            "Producto tecnologico de adaptacion": "misc",
            "Producto tecnologico de innovacion": "misc",
            "Puntaje Asignado a Profesor Visitante": "misc",
            "Reporte de caso en libro": "works",
            "Reporte de caso en libro de texto": "works",
            "Reporte de caso en libro resultado de investigacion": "works",
            "Reporte de caso en revista Tipo A1": "works",
            "Reporte de caso en revista Tipo A2": "works",
            "Reporte de caso en revista Tipo B": "works",
            "Reporte de caso en revista Tipo C": "works",
            "Resena critica": "works",
            "Resumen de ponencia en evento iberoamericano o de 2 continet": "misc",
            "Resumen de ponencia en evento internacional ()": "misc",
            "Resumen de ponencia en evento latinoamerican o de 1 continet": "misc",
            "Resumen de ponencia en evento nacional ()": "misc",
            "Revision de tema en libro de difusion nacional-intenacional": "works",
            "Revision de tema en libro de texto": "works",
            "Revision de tema en libro resultado de investigacion": "works",
            "Revision de tema en revista Tipo A1": "works",
            "Revision de tema en revista Tipo A2": "works",
            "Revision de tema en revista Tipo B": "works",
            "Revision de tema en revista Tipo C": "works",
            "Software de produccion cientifica": "misc",
            "Software de produccion tecnologica": "misc",
            "Traduccion Articulo": "works",
            "Traduccion Articulo de revista o libro de difusion nal o reg": "works",
            "Traduccion de articulo o capitulo de libro": "works",
            "Traduccion de Libro": "works",
            "Video  didactico internacional": "misc",
            "Video  didactico nacional": "misc",
            "Video didactico de difusion local": "misc",
            "Video Documental Internacional": "misc",
            "Video Documental Local": "misc",
            "Video Documental Nacional": "misc"
        },
        "https://ror.org/00jb9vg53": {
            "1.TEXTO UNIVERSITARIO": "works",
            "3.ENSAYOS EN FORMA DE ARTíCULOS": "works",
            "4.MóDULOS O MATERIALES AUTOFORMATIVOS": "misc",
            "5.CONFERENCIAS DE CLASE": "misc",
            "6.GUíAS DE PRáCTICA, TALLER O LABORATORIO": "misc",
            "8.MATERIALES AUDIOVISUALES": "misc",
            "ADAPTACIóN TECNOLóGICA": "misc",
            "ARTICULO EN REVISTA NO INDEXADA/HOMOLOGADA": "works",
            "CARáCTER DOCUMENTAL IMPACTO INTERNACIONAL": "misc",
            "COMUNICACION CORTA REVISTA TIPO A1": "works",
            "COMUNICACION CORTA REVISTA TIPO A2": "works",
            "COMUNICACION CORTA REVISTA TIPO B": "works",
            "COMUNICACION CORTA REVISTA TIPO C": "works",
            "CREACION COMPLEMENTARIA IMPACTO REGIONAL - LOCAL": "misc",
            "CREACION ORIGINAL IMPACTO REGIONAL - LOCAL": "misc",
            "DESARROLLO SOFTWARE PRODUCCION CIENTIFICA": "misc",
            "DESARROLLO SOFTWARE PRODUCCION TECNOLOGICA": "misc",
            "DIRECCION DE TESIS DE DOCTORADO": "misc",
            "DIRECCION DE TESIS DE MAESTRIA": "misc",
            "DISCOS, FILMES, VIDEOS Y AUDIOVISUALES": "misc",
            "DISEÑOS O MEMORIAS TÉCNICAS Y PROTOTIPOS": "misc",
            "DOCUMENTOS DE ANALOGOS FINES Y CONTENIDOS": "misc",
            "DOCUMENTOS DE TRABAJO DE INVESTIGACION": "works",
            "DOCUMENTOS SOBRE POLÍTICA UNIVERSITARIA": "misc",
            "EN REVISTA TIPO A1": "works",
            "EN REVISTA TIPO A2": "works",
            "EN REVISTA TIPO B": "works",
            "EN REVISTA TIPO C": "works",
            "ESTUDIOS POSTDOCTORALES": "misc",
            "FINES DIDáCTICOS IMPACTO NACIONAL": "misc",
            "FULL PAPER REVISTA TIPO A1": "works",
            "FULL PAPER REVISTA TIPO A2": "works",
            "FULL PAPER REVISTA TIPO B": "works",
            "FULL PAPER REVISTA TIPO C": "works",
            "IMPACTO INTERNACIONAL": "misc",
            "IMPACTO NACIONAL": "misc",
            "INFORMES FINALES DE INVESTIGACION": "misc",
            "INNOVACIóN TECNOLóGICA": "misc",
            "INTERPRETACION DE IMPACTO REGIONAL - LOCAL": "misc",
            "INVENTO PATENTADO": "patents",
            "LIBRO DE ENSAYO": "works",
            "LIBRO DE INVESTIGACION": "works",
            "LIBRO DE INVESTIGACION_": "works",
            "LIBRO DE SISTEMATIZACION": "works",
            "LIBRO DE TEXTO": "works",
            "MATERIALES DE SOPORTE A LA DOCENCIA": "misc",
            "MATERIALES PARA EDUCACION A DISTANCIA": "misc",
            "MONOGRAFIA": "works",
            "MONOGRAFIA DE SISTEMATIZACION": "works",
            "OBRAS ARQUITECTÓNICAS": "misc",
            "PATENTE": "patents",
            "PONENCIA": "events",
            "PONENCIA EN EVENTO INTERNACIONAL": "events",
            "PONENCIA EN EVENTO NACIONAL": "events",
            "PONENCIA EN EVENTO REGIONAL": "events",
            "PONENCIAS PRESENTADAS EN CONGRESOS": "events",
            "PREMIO INTERNACIONAL": "misc",
            "PREMIO NACIONAL": "misc",
            "PROFESOR DISTINGUIDO, HONORARIO ó EMéRITO": "misc",
            "RECONOCIMIENTO ESPECIAL": "misc",
            "REPORTE, REVISION DE TEMA EN REVISTA TIPO A1": "works",
            "REPORTE, REVISION DE TEMA EN REVISTA TIPO A2": "works",
            "REPORTE, REVISION DE TEMA EN REVISTA TIPO B": "works",
            "REPORTE, REVISION DE TEMA EN REVISTA TIPO C": "works",
            "REPRESENTACIóN ARTISTICA": "misc",
            "RESENAS CRITICAS": "works",
            "RESEñAS CRíTICAS": "works",
            "REVISTA NO INDEXADA/HOMOLOGADA": "works",
            "REVISTA NO INDEXADA-HOMOLOGADA": "works",
            "TESIS DE POSTGRADO LAUREADA O EQUIVALENTE": "works",
            "TESIS DOCTORADO": "works",
            "TESIS MAESTRIA": "works",
            "TRADUCCIóN DE LIBRO": "works",
            "TRADUCCION PUBLICADA DE ARTICULO": "works",
        },
        "https://ror.org/059yx9a68": {
            "Artículo de revista": "works",
            "Tesis Maestría": "works",
            "Capítulo de libro": "works",
            "Estado del arte": "works",
            "Formato audiovisual": "misc",
            "Ponencias en eventos especializados": "events",
            "Tesis Doctorado": "works",
            "Editorial": "works",
            "Tesis Especialización": "works",
            "Errata": "works",
            "Libro": "works",
            "Artículo de conferencia": "works",
            "Revisión sistemática": "works",
            "Reporte de caso": "works",
            "Patente": "patents",
            "Tesis Pregrado": "works",
            "Desarrollo de software": "misc",
            "Apoyo a la investigación": "misc",
            "Preimpresión": "works",
            "Proyecto": "misc",
            "Comentario": "works",
            "Estudio comparativo": "works",
            "Estudio observacional": "works",
            "Proceso instrumental": "misc",
            "Colección científica": "works",
            "Reporte técnico": "works",
            "Datos": "misc",
            "Posters presentados": "events",
            "Ponencias en eventos": "events",
            "Biografía": "works"
        }
    }

    # Validate ROR code
    if ror_code not in ciarp_data_types:
        raise ValueError("ROR code not found")

    # Validate entity
    if entity not in ["works", "patents", "events", "misc"]:
        raise ValueError("Entity not found")

    # Filter categories by entity
    institution_data = ciarp_data_types[ror_code]
    filtered_categories = [
        category for category, category_type in institution_data.items()
        if category_type == entity
    ]

    return filtered_categories
