import { Component, OnInit } from '@angular/core';

import { Myapp } from './myapp';
import { MyappService } from './myapp.service';

@Component({
  selector: 'myapp-root',
  templateUrl: './myapp.component.html',
  styleUrls: ['./myapp.component.css']
})

export class MyappComponent implements OnInit {

  myapp: Myapp[];
  title = 'myapp';

  constructor(
    private myappService: MyappService
  ) { }

  getMyapp(): void {
    this.myappService.getMyapp().then(myapp => {
      this.myapp = myapp;
    });
  }

  ngOnInit(): void {
    this.getMyapp();
  }
}
