import './App.less'
import { Button, notification } from 'antd'
import { useCallback } from 'react'

export default function App() {
  const runProcess = useCallback(async () => {
    try {
      const response = await fetch('/api/run-process', { method: 'POST' })
      
      if (response.status === 200) {
        const processId = response.text()
        notification.info({
          message: 'Process Running',
          description: `A very long process with id ${processId} is ongoing`
        })
      } else {
        notification.error({
          message: 'Error Running Process',
          description: `Status: ${response.status}`
        })
      }


    } catch(err) {
      notification.error({
        message: 'Error Running Process',
        description: err
      })
    }
  }, [])

  return (
    <div className="App">
      <Button 
        size="large" 
        type="primary"
        onClick={runProcess}
      >
        Run process
      </Button>
    </div>
  )
}
