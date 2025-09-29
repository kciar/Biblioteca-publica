// src/pages/Dashboard.jsx
import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";

export default function Dashboard() {
  return (
    <div>
      <Navbar />
      <h2>Dashboard</h2>
      <ul>
        <li><Link to="/livros">Gerenciar Livros</Link></li>
        <li><Link to="/emprestimos">Gerenciar Empréstimos</Link></li>
      </ul>
    </div>
  );
}
