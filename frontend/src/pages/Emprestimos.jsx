// src/pages/Emprestimos.jsx
import { useEffect, useState } from "react";
import api from "../api/axios";
import Navbar from "../components/Navbar";

export default function Emprestimos() {
  const [emprestimos, setEmprestimos] = useState([]);
  const [usuarios, setUsuarios] = useState([]);
  const [livros, setLivros] = useState([]);
  const [form, setForm] = useState({ usuario: "", livro: "" });

  // Buscar empréstimos, usuários e livros
  async function fetchData() {
    try {
      const [resEmp, resUser, resLivros] = await Promise.all([
        api.get("emprestimos/"),
        api.get("usuarios/"),
        api.get("livros/?disponivel=true"), // só livros disponíveis
      ]);
      setEmprestimos(resEmp.data);
      setUsuarios(resUser.data);
      setLivros(resLivros.data);
    } catch (err) {
      console.error(err);
    }
  }

  useEffect(() => {
    fetchData();
  }, []);

  // Criar novo empréstimo
  async function handleSubmit(e) {
    e.preventDefault();
    try {
      await api.post("emprestimos/", form);
      setForm({ usuario: "", livro: "" });
      fetchData();
    } catch (err) {
      console.error(err);
    }
  }

  // Marcar como devolvido
  async function handleDevolver(id) {
    try {
      await api.patch(`emprestimos/${id}/`, { status: "DEVOLVIDO" });
      fetchData();
    } catch (err) {
      console.error(err);
    }
  }

  // Excluir empréstimo
  async function handleDelete(id) {
    try {
      await api.delete(`emprestimos/${id}/`);
      fetchData();
    } catch (err) {
      console.error(err);
    }
  }

  return (
    <div>
      <Navbar />
      <h2>Empréstimos</h2>

      <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
        <select
          value={form.usuario}
          onChange={(e) => setForm({ ...form, usuario: e.target.value })}
          required
        >
          <option value="">Selecionar usuário</option>
          {usuarios.map((u) => (
            <option key={u.id} value={u.id}>{u.username}</option>
          ))}
        </select>

        <select
          value={form.livro}
          onChange={(e) => setForm({ ...form, livro: e.target.value })}
          required
        >
          <option value="">Selecionar livro</option>
          {livros.map((l) => (
            <option key={l.id} value={l.id}>{l.titulo}</option>
          ))}
        </select>

        <button type="submit">Registrar Empréstimo</button>
      </form>

      <ul>
        {emprestimos.map((e) => (
          <li key={e.id}>
            {e.livro.titulo} → {e.usuario.username} ({e.status})
            {e.status === "EM_ANDAMENTO" && (
              <button onClick={() => handleDevolver(e.id)}>Devolver</button>
            )}
            <button onClick={() => handleDelete(e.id)}>Excluir</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
