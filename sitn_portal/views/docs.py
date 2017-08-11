# -*- coding: utf-8 -*-
from pyramid.view import view_config


@view_config(route_name='docs', renderer='docs.html')
def docs(request):

    return {'one': 'one', 'project': 'sitn_portal'}


@view_config(route_name='documents', renderer='json')
def documents(request):

	if request.host_url == 'http://localhost:6543':
		request.response.headers['Access-Control-Allow-Origin'] = '*'

	docs = [
      {
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
      },
      {
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
      },
      {
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
      }
    ]

	return { 'documents': docs}
