import React, { useState, useEffect } from "react"
import Typography from '@mui/material/Typography';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import List from '@mui/material/List';

function generate(element) {
    return [1, 2, 3].map((value) =>
        React.cloneElement(element, {
            key: value,
        }),
    );
}

export default function ListComponent(props) {
    const [secondary, setSecondary] = React.useState(false);

    return (
        <div>
            <Typography sx={{ mt: 4, mb: 2 }} variant="h6" component="div">
                Text only
            </Typography>
            <List>
                {generate(
                    <ListItem>
                        <ListItemText
                            primary="Single-line item"
                            secondary={secondary ? 'Secondary text' : null}
                        />
                    </ListItem>
                )}
            </List>
        </div>
    )
} 
