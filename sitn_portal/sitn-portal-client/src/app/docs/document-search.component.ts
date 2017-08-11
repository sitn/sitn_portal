import { Component, OnInit } from '@angular/core';
import { Router }            from '@angular/router';

import { Observable }        from 'rxjs/Observable';
import { Subject }           from 'rxjs/Subject';

// Observable class extensions
import 'rxjs/add/observable/of';

// Observable operators
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/debounceTime';
import 'rxjs/add/operator/distinctUntilChanged';

import { DocumentSearchService } from './document-search.service';
import { Document } from './document';

@Component({
  selector: 'document-search',
  templateUrl: './document-search.component.html',
  styleUrls: [ './document-search.component.css' ],
  providers: [DocumentSearchService]
})
export class DocumentSearchComponent implements OnInit {
  documents: Observable<Document[]>;
  private searchTerms = new Subject<string>();

  constructor(
    private documentSearchService: DocumentSearchService,
    private router: Router) {}

  // Push a search term into the observable stream.
  search(term: string): void {
    this.searchTerms.next(term);
  }

  ngOnInit(): void {
    this.documents = this.searchTerms
      .debounceTime(300)        // wait 300ms after each keystroke before considering the term
      .distinctUntilChanged()   // ignore if next search term is same as previous
      .switchMap(term => term   // switch to new observable each time the term changes
        // return the http search observable
        ? this.documentSearchService.search(term)
        : Observable.of<Document[]>([]))
      .catch(error => {
        // TODO: add real error handling
        console.log(error);
        return Observable.of<Document[]>([]);
      });
  }

  gotoDetail(document: Document): void {
    let link = ['/docdetail', document.docid];
    this.router.navigate(link);
  }
}
