import { useState, useEffect } from 'react'
import { toast } from 'sonner'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table'
import { Spinner } from '@/components/ui/spinner'
import { getClients } from '@/services/clientService'
import type { Client } from '@/types/client'

export function ClientsPage() {
  const [clients, setClients] = useState<Client[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  async function loadClients() {
    setLoading(true)
    setError(null)
    try {
      setClients(await getClients())
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => { loadClients() }, [])

  return (
    <Card className="max-w-2xl">
      <CardHeader><CardTitle>Clients</CardTitle></CardHeader>
      <CardContent>
        {loading && <div className="flex justify-center py-10"><Spinner /></div>}
        {error && <p className="text-center py-10 text-destructive">⚠ {error}</p>}
        {!loading && !error && clients.length === 0 && (
          <p className="text-center py-10 text-muted-foreground">No clients found.</p>
        )}
        {!loading && !error && clients.length > 0 && (
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>ID</TableHead>
                <TableHead>Name</TableHead>
                <TableHead>National Number</TableHead>
                <TableHead />
              </TableRow>
            </TableHeader>
            <TableBody>
              {clients.map(c => (
                <TableRow key={c.id}>
                  <TableCell>{c.id}</TableCell>
                  <TableCell>{c.name}</TableCell>
                  <TableCell><Badge variant="outline">{c.national_number}</Badge></TableCell>
                  <TableCell className="text-right">
                    <Button size="sm" variant="outline" onClick={() => toast.info(`Viewing client ${c.name}`)}>View →</Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        )}
      </CardContent>
    </Card>
  )
}
