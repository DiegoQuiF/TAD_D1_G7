import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Figura5Component } from './figura5.component';

describe('Figura5Component', () => {
  let component: Figura5Component;
  let fixture: ComponentFixture<Figura5Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Figura5Component]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(Figura5Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
