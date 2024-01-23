import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrearColeccionComponent } from './crear-coleccion.component';

describe('CrearColeccionComponent', () => {
  let component: CrearColeccionComponent;
  let fixture: ComponentFixture<CrearColeccionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CrearColeccionComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CrearColeccionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
