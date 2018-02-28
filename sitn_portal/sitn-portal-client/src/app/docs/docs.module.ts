import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { HttpModule }    from '@angular/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { DocumentRoutingModule }     from './document-routing.module';

import { DocsComponent } from './docs.component';
import { DocumentFormComponent } from './document-form.component';
import { DocumentDetailComponent } from './document-detail.component';
import { DocumentListComponent } from './document-list.component';
import { DocumentSearchComponent } from './document-search.component';
import { DocumentService } from './document.service';

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    DocumentRoutingModule,
    NgbModule.forRoot()
  ],
  declarations: [
    DocsComponent,
    DocumentFormComponent,
    DocumentListComponent,
    DocumentDetailComponent,
    DocumentSearchComponent
  ],
  providers: [DocumentService],
  bootstrap: [DocsComponent]

})
export class DocsModule { }
