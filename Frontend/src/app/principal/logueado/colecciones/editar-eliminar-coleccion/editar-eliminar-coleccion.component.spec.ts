import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditarEliminarColeccionComponent } from './editar-eliminar-coleccion.component';

describe('EditarEliminarColeccionComponent', () => {
  let component: EditarEliminarColeccionComponent;
  let fixture: ComponentFixture<EditarEliminarColeccionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EditarEliminarColeccionComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EditarEliminarColeccionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
