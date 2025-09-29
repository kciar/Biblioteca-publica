// src/components/LivroForm.jsx
import { useState, useEffect } from "react";
import api from "../api/axios";

export default function LivroForm({ livro, onSuccess }) {
  const [form, setForm] = useState({ titulo: "", autor: "", ano: "", genero: "" });

  useEffect(() => {
    if (livro) setForm(livro);
  }, [livro]);

  async function handleSubmit(e) {
    e.preventDefault();
    if (livro?.id) {
      await api.put(`livros/${livro.id}/`, form);
    } else {
      await api.post("livros/", form);
    }
    setForm({ titulo: "", autor: "", ano: "", genero: "" });
    if (onSuccess) onSuccess();
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="titulo" value={form.titulo} onChange={(e) => setForm({ ...form, titulo: e.target.value })} placeholder="Título" required />
      <input name="autor" value={form.autor} onChange={(e) => setForm({ ...form, autor: e.target.value })} placeholder="Autor" />
      <input name="ano" type="number" value={form.ano} onChange={(e) => setForm({ ...form, ano: e.target.value })} placeholder="Ano" />
      <input name="genero" value={form.genero} onChange={(e) => setForm({ ...form, genero: e.target.value })} placeholder="Gênero" />
      <button type="submit">{livro ? "Atualizar" : "Adicionar"}</button>
    </form>
  );
}
