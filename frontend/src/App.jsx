// src/App.jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Livros from "./pages/Livros";
import Emprestimos from "./pages/Emprestimos";
import PrivateRoute from "./components/PrivateRoute";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Login */}
        <Route path="/login" element={<Login />} />

        {/* Rotas privadas */}
        <Route path="/" element={<PrivateRoute><Dashboard /></PrivateRoute>} />
        <Route path="/livros" element={<PrivateRoute><Livros /></PrivateRoute>} />
        <Route path="/emprestimos" element={<PrivateRoute><Emprestimos /></PrivateRoute>} />
      </Routes>
    </BrowserRouter>
  );
}
