// src/pages/Livros.jsx
import { useEffect, useState } from "react";
import api from "../api/axios";
import LivroForm from "../components/LivroForm";
import Navbar from "../components/Navbar";

export default function Livros() {
  const [livros, setLivros] = useState([]);
  const [editLivro, setEditLivro] = useState(null);

  async function fetchLivros() {
    const res = await api.get("livros/");
    setLivros(res.data);
  }

  useEffect(() => {
    fetchLivros();
  }, []);

  async function handleDelete(id) {
    await api.delete(`livros/${id}/`);
    fetchLivros();
  }

  return (
    <div>
      <Navbar />
      <h2>Livros</h2>
      <LivroForm livro={editLivro} onSuccess={fetchLivros} />
      <ul>
        {livros.map((l) => (
          <li key={l.id}>
            {l.titulo} — {l.autor}
            <button onClick={() => setEditLivro(l)}>Editar</button>
            <button onClick={() => handleDelete(l.id)}>Excluir</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
