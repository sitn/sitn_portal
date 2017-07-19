import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';

import { MyappComponent } from './myapp.component';
import { MyappService } from './myapp.service';

@NgModule({
  declarations: [
    MyappComponent
  ],

  imports: [
    BrowserModule,
    HttpModule
  ],

  providers: [
    MyappService
  ],

  bootstrap: [MyappComponent]

})
export class MyappModule { }
