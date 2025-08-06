import { useEffect, useState } from 'react';
import * as Papa from 'papaparse';
import { DataGrid } from '@mui/x-data-grid';
import type { GridColDef, GridRenderCellParams } from '@mui/x-data-grid';

import Box from '@mui/material/Box';
import './ResultsTable.scss';

interface Record {
  id: number;
  LocalDateTime: string;
  State: string;
  TowerJump: string;
  Confidence: string;
  Valid: string;
}

export function ResultsTable() {
  const [rows, setRows] = useState<Record[]>([]);

  useEffect(() => {
    fetch('/output/tower_jump_analysis.csv')
      .then((res) => res.text())
      .then((text) => {
        const parsed = Papa.parse<Omit<Record, 'id'>>(text, {
          header: true,
          skipEmptyLines: true,
        });

        const withIds = parsed.data.map((row, index) => ({
          id: index + 1,
          ...row,
        }));

        setRows(withIds as Record[]);
      });
  }, []);

  const columns: GridColDef[] = [
    { field: 'LocalDateTime', headerName: 'Date', flex: 1 },
    { field: 'State', headerName: 'State', flex: 1 },
    {
      field: 'TowerJump',
      headerName: 'Tower Jump',
      flex: 1,
      renderCell: (params: GridRenderCellParams) => <span>{params.value}</span>,
    },
    {
      field: 'Confidence',
      headerName: 'Confidence (%)',
      flex: 1,
      type: 'number',
    },
    {
      field: 'Valid',
      headerName: 'Valid',
      flex: 1,
      renderCell: (params: GridRenderCellParams) => <span>{params.value}</span>,
    },
  ];

  return (
    <Box sx={{ height: 800, width: '100%', p: 4 }}>
      <h2>Tower Jump Report</h2>
      <DataGrid
        rows={rows}
        columns={columns}
        initialState={{
          pagination: { paginationModel: { pageSize: 20, page: 0 } },
        }}
        pageSizeOptions={[20, 50, 100]}
        disableRowSelectionOnClick
        getRowClassName={(params) =>
          params.row.Valid === 'False'
            ? 'invalid-row'
            : params.row.TowerJump === 'Yes'
            ? 'jump-row'
            : 'valid-row'
        }
      />
    </Box>
  );
}
