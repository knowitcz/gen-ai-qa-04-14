import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider, Navigate } from 'react-router-dom'
import { TooltipProvider } from '@/components/ui/tooltip'
import './index.css'
import { AppLayout } from '@/components/AppLayout'
import { ClientsPage } from '@/pages/ClientsPage'

const router = createBrowserRouter([
  {
    element: <AppLayout />,
    children: [
      { path: '/clients', element: <ClientsPage />, handle: { breadcrumb: 'Clients' } },
      { path: '*', element: <Navigate to="/clients" replace /> },
    ],
  },
])

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <TooltipProvider>
      <RouterProvider router={router} />
    </TooltipProvider>
  </StrictMode>,
)
