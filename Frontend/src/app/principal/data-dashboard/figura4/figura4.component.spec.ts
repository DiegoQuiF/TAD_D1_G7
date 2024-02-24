import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Figura4Component } from './figura4.component';

describe('Figura4Component', () => {
  let component: Figura4Component;
  let fixture: ComponentFixture<Figura4Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Figura4Component]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(Figura4Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
