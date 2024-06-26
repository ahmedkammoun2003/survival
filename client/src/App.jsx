import { useState } from 'react'
import './App.css'
import MapComponent from "./components/MapComponent"
import Chatbot from './components/Chatbot'
import Article from './components/Article'

function App() {

  return (
    <>
      <MapComponent/>
      <Chatbot/>
      <Article/>
    </>
  )
}

export default App
