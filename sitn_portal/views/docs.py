# -*- coding: utf-8 -*-
from pyramid.view import view_config

from sitn_portal.models import DBSession
from sitn_portal.models import Documents

@view_config(route_name='docs', renderer='docs.html')
def docs(request):

    return {'one': 'one', 'project': 'sitn_portal'}

@view_config(route_name='get', renderer='docs.html')
def get(request, docid):

    return {'document': 'docid'}

@view_config(route_name='list', renderer='json')
def list(request, docid=None):
    if request.host_url == 'http://localhost:6543':
        request.response.headers['Access-Control-Allow-Origin'] = '*'

    documents = DBSession.query(Documents).order_by(
                Documents.docid.asc()).all()
    doclist = []
    for document in documents:
        doclist.append({
            'docid': document.docid,
            'doctype': document.doctype,
            'lang': document.lang,
            'state': document.state,
            'chmunicipalitynb': document.chmunicipalitynb,
            'municipalitynb': document.municipalitynb,
            'municipalityname': document.municipalityname,
            'cadastrenb': document.cadastrenb,
            'title': document.title,
            'officialtitle': document.officialtitle,
            'abbreviation': document.abbreviation,
            'officialnb': document.officialnb,
            'legalstate': document.legalstates.value,
            'remoteurl': document.remoteurl,
            'localurl': document.localurl,
            'sanctiondate': document.sanctiondate.isoformat()
            if document.sanctiondate else None,
            'abolishingdate': document.abolishingdate.isoformat()
            if document.abolishingdate else None,
            'entrydate': document.entrydate.isoformat()
            if document.entrydate else None,
            'publicationdate': document.publicationdate.isoformat()
            if document.publicationdate else None,
            'revisiondate': document.revisiondate.isoformat()
            if document.revisiondate else None,
            'operator': document.operator
        })
    docs = [{
        'docid': 'NE0000D199110020001fr',
        'legalstate': 1,
        'abbreviation': 'LCAT',
        'sanctiondate': '',
        'operator': 'acn\\voisardf',
        'localurl': '',
        'chmunicipalitynb': 0,
        'municipalitynb': 0,
        'title': '',
        'state': 'NE',
        'publicationdate': '1991-10-02',
        'officialtitle': 'Loi cantonale sur l\'aménagement du territoire',
        'officialnb': 'RSN 701.0',
        'remoteurl': 'http://rsn.ne.ch/ajour/dati/f/pdf/7010.pdf',
        'revisiondate': '',
        'lang': 'fr',
        'abolishingdate': '',
        'doctype': 1,
        'cadastrenb': 0,
        'municipalityname': '',
        'entrydate': ''
        }, {
        'docid': 'BL0000D199110020002de',
        'legalstate': 1,
        'abbreviation': 'LCAT',
        'sanctiondate': '',
        'operator': 'acn\\voisardf',
        'localurl': '',
        'chmunicipalitynb': 0,
        'municipalitynb': 0,
        'title': '',
        'state': 'BL',
        'publicationdate': '1991-10-02',
        'officialtitle': 'Loi cantonale sur l\'aménagement du territoire',
        'officialnb': 'RSN 701.0',
        'remoteurl': 'http://rsn.ne.ch/ajour/dati/f/pdf/7010.pdf',
        'revisiondate': '',
        'lang': 'de',
        'abolishingdate': '',
        'doctype': 1,
        'cadastrenb': 0,
        'municipalityname': '',
        'entrydate': ''
        }, {
        'docid': 'NE0000D199110020003fr',
        'legalstate': 1,
        'abbreviation': 'LCAT',
        'sanctiondate': '1991-10-02',
        'operator': 'acn\\voisardf',
        'localurl': '',
        'chmunicipalitynb': 0,
        'municipalitynb': 0,
        'title': '',
        'state': 'NE',
        'publicationdate': '',
        'officialtitle': 'Loi cantonale sur l\'aménagement du territoire',
        'officialnb': 'RSN 701.0',
        'remoteurl': 'http://rsn.ne.ch/ajour/dati/f/pdf/7010.pdf',
        'revisiondate': '',
        'lang': 'fr',
        'abolishingdate': '',
        'doctype': 1,
        'cadastrenb': 0,
        'municipalityname': '',
        'entrydate': '1991-10-02',
        }]

    return {'documents': doclist}
