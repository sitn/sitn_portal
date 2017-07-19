import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';

import { DocsComponent } from './docs.component';
import { DocService } from './doc.service';

@NgModule({
  declarations: [
    DocsComponent
  ],

  imports: [
    BrowserModule,
    HttpModule
  ],

  providers: [
    DocService
  ],

  bootstrap: [DocsComponent]

})
export class DocsModule { }
