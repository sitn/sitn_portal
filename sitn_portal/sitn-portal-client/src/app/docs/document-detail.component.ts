import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { Location }                 from '@angular/common';

import { DocumentService } from './document.service';
import { Document } from './document';
import 'rxjs/add/operator/switchMap';

@Component({
  selector: 'document-detail',
  templateUrl: './document-detail.component.html',
  styleUrls: [ './document-detail.component.css' ],
})
export class DocumentDetailComponent implements OnInit {
  @Input() document: Document;
  @Input() err: 'error!';

  constructor(
    private documentService: DocumentService,
    private route: ActivatedRoute,
    private location: Location
  ) {}

  ngOnInit(): void {
    this.route.paramMap
      .switchMap((params: ParamMap) => this.documentService.getDocument(params.get('docid')))
      .subscribe(
        document => this.document = document,
        err => this.err = err
      );
  }

  goBack(): void {
    this.location.back();
  }
}
