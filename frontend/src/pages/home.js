import React from 'react';
import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div className="text-center">
      <h1>Bienvenidos</h1>
      <p className="lead">Mi Tienda online</p>
      
      <div className="mt-4">
        <Link to="/login" className="btn btn-primary m-2">Iniciar sesión</Link>
        <Link to="/admin" className="btn btn-secondary m-2">Ir al panel admin</Link>
        <Link to="/admin/categories" className="btn btn-info m-2">Gestionar categorías</Link>
      </div>
    </div>
  );
}
