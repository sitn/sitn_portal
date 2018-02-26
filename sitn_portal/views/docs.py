# -*- coding: utf-8 -*-
from pyramid.view import view_config

from sitn_portal.models import DBSession
from sitn_portal.models import Documents


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

    return {'documents': doclist}
