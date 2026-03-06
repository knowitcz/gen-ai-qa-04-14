import type { Client } from '@/types/client'

const API = '/api/v1'

export async function getClients(): Promise<Client[]> {
  const res = await fetch(`${API}/client`)
  if (!res.ok) throw new Error('Failed to load clients')
  return res.json()
}
