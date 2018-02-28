# -*- coding: utf-8 -*-
from pyramid.view import view_config

from simplejson import loads

from sqlalchemy import or_
from sqlalchemy.orm import relationship, backref

from sitn_portal.models import DBSession
from sitn_portal.models import Documents


@view_config(route_name='add', renderer='json')
def add(request):
    """ Function to add a new document to the database
    """
    data = sloads(request.POST['data'])

    return data


@view_config(route_name='edit', renderer='docs.html')
def edit(request, docid):
    """ Function to edit an existing document
    """
    return 'edit'


@view_config(route_name='delete', renderer='docs.html')
def delete(request, docid):
    """ Function to remove/archive a document from the database
    """
    return 'delete'


@view_config(route_name='get', renderer='json')
def get(request):
    """ Gets a document based on it's docid. A single result is expected.
    """

    try:
        # if no docid is given the function throws an error
        docid = request.matchdict['docid']
    except:
        error = 'Erreur. Il manque un identifiant de document.'
        return error

    results = DBSession.query(Documents).filter(Documents.docid.like("%"+docid+"%")).order_by(
                Documents.docid.asc()).all()

    # if there is more than one document with the same docid an error is thrown
    if (len(results) > 1):
        error = 'Erreur. l\'identifiant de document n\'est pas unique.'
        return error
    else:
        result = DBSession.query(Documents).filter(Documents.docid == docid).first()
        document = {
            'docid': result.docid,
            'doctype': result.doctype,
            'lang': result.lang,
            'state': result.state,
            'chmunicipalitynb': result.chmunicipalitynb,
            'municipalitynb': result.municipalitynb,
            'municipalityname': result.municipalityname,
            'cadastrenb': result.cadastrenb,
            'title': result.title,
            'officialtitle': result.officialtitle,
            'abbreviation': result.abbreviation,
            'officialnb': result.officialnb,
            'legalstate': result.legalstates.value,
            'remoteurl': result.remoteurl,
            'localurl': result.localurl,
            'sanctiondate': result.sanctiondate.isoformat()
            if result.sanctiondate else None,
            'abolishingdate': result.abolishingdate.isoformat()
            if result.abolishingdate else None,
            'entrydate': result.entrydate.isoformat()
            if result.entrydate else None,
            'publicationdate': result.publicationdate.isoformat()
            if result.publicationdate else None,
            'revisiondate': result.revisiondate.isoformat()
            if result.revisiondate else None,
            'operator': result.operator
        }

    return {'document': document}


@view_config(route_name='search', renderer='json')
def search(request):
    """ Function to search for a document by its docid or
        by its official title.
        Returns a list of documents matching the search criteria

        Args:
        term (string): The search term
    """
    term = request.matchdict['term']

    documents = DBSession.query(Documents).filter(or_(
                    Documents.officialtitle.like("%"+term+"%"),
                    Documents.docid.like("%"+term+"%")
                    )).order_by(Documents.docid.asc()).all()

    docs = []
    for document in documents:
        docs.append({
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

    return {'documents': docs}


@view_config(route_name='list', renderer='json')
def list(request):
    """ Function to list all documents in the database.
        Returns a document list as dict.
    """
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
